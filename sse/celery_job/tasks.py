import json
from pathlib import Path

import redis
from celery import shared_task
from django_celery_beat.models import PeriodicTask

from api.models import CrontabExecID
from api.models import ExecutionRecord
from api.models import ExecutionRequestBackup
from sse.lib.utils.config_parser import ConfigParser
from sse.lib.utils.dictUitls import parser_counts_by_task, delete_dict_by_task
from sse.lib.utils.logger import logger
from sse.lib.utils.rabbitMq import AMQP

redis_info = ConfigParser().getRedis
rds = redis.Redis(**redis_info, decode_responses=True)
period_task_names_and_counts = []
cron_task_names = []
rds.set("period_task_names_and_counts", json.dumps(period_task_names_and_counts, ensure_ascii=False))
rds.set("cron_task_names", json.dumps(cron_task_names, ensure_ascii=False))

logger = logger()

host, port, user, password, virtual_host, exchange, request_queue, reply_queue = ConfigParser().read_mq_info

BASE_DIR = Path(__file__).resolve().parent.parent


def reset_gte3_count(period_obj):
    period_obj.enabled = False
    period_obj.total_run_count = 0
    period_obj.save()


@shared_task
def celery_update(response, *args, **kwargs):
    """
    取得执行引擎的结果，并将数据结果更新excutionrecord表中
    @param exec_id: 执行编码
    @param duration: 执行耗时
    @param path: ftp服务器上的报告路径
    """
    exec_id = response.get('exec_id')
    try:
        record = ExecutionRecord.objects.get(code=exec_id)
        if response["success"] == True:
            record.statue = 0
        else:
            record.statue = 3
        record.duration = response["duration"]
        record.path = response['path']

        if record.task_type == 1:  # 定时任务
            record.cron_task_status = 2
            task_name = CrontabExecID.objects.get(code=exec_id).task
            cron_task_names = json.loads(rds.get("cron_task_names"))
            cron_task_names.append(task_name)
            rds.set("cron_task_names", json.dumps(cron_task_names))

        elif record.task_type == 2:  # 轮询任务
            crontab_obj = CrontabExecID.objects.get(code=exec_id)
            task_counts = {"task": crontab_obj.task, "counts": 0}
            period_task_names_and_counts = json.loads(rds.get("period_task_names_and_counts"))

            counts = parser_counts_by_task(crontab_obj.task, period_task_names_and_counts)
            if counts != None:
                period_task_names_and_counts = delete_dict_by_task(crontab_obj.task, period_task_names_and_counts)
                if counts < 1:
                    counts += 1
                    task_counts.update(counts=counts)
                    period_task_names_and_counts.append(task_counts)
                else:
                    record.cron_task_status = 2
                    period_obj = PeriodicTask.objects.get(name=crontab_obj.task)
                    period_obj.enabled = False
                    period_obj.total_run_count = 0
                    period_obj.save()
            else:
                period_task_names_and_counts.append(task_counts)
            rds.set("period_task_names_and_counts", json.dumps(period_task_names_and_counts))

        record.save()
    except Exception as e:
        logger.error(f"Fail to update exec_id:[{exec_id}],due to error ;{str(e)}")
    else:
        logger.debug(f"Success to update a record with exec_id:[{exec_id}]")


@shared_task
def celery_exec_request(message: dict, rerun_flag=False):
    """
    todo:核心代码
    将执行的参数通过MQ发给执行引擎，异步执行
    @param message: message = {"exec_id":"","body":[]}
    """

    code = message.get("exec_id")
    logger.info(f"Publish execution: [{code}] to MQ and backup request information.")
    ExecutionRecord.objects.filter(code=code).update(statue=1)

    if not rerun_flag:
        try:
            ExecutionRequestBackup.objects.create(
                code=code,
                body=message
            )
        except Exception:
            ExecutionRequestBackup.objects.filter(code=code).update(  # 若果已存在则更新下Body数据
                body=message
            )

    try:
        exec_request_mq = AMQP()
        exec_request_mq.basic_publish(message, "pytest.exec.report")
    except Exception as e:
        logger.error(f"Fail to publish message to execution engine,errors as following:{str(e)}.")
