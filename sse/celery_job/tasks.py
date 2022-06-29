import os
import ast
import datetime
import time
from pathlib import Path
from sse.lib.utils.rabbitMq import AMQP
from api.models import ExecutionRecord
from sse.lib.utils.config_parser import ConfigParser
from sse.lib.utils.logger import logger
from api.models import ExecutionRequestBackup
from celery import shared_task

logger = logger()

host, port, user, password, virtual_host, exchange, request_queue,reply_queue = ConfigParser().read_mq_info

BASE_DIR = Path(__file__).resolve().parent.parent

@shared_task
def celery_update(response,*args,**kwargs):
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
        record.save()
    except Exception:
        logger.error(f"Fail to update exec_id:[{exec_id}]")
    else:
        logger.debug(f"Success to update a record with exec_id:[{exec_id}]")

@shared_task
def celery_exec_request(message:dict,re_flag=False):
    """
    todo:核心代码
    将执行的参数通过MQ发给执行引擎，异步执行
    @param message: message = {"exec_id":"","body":[]}
    """
    logger.info("Publish message to MQ and backup request information.")
    if not re_flag:
        ExecutionRequestBackup.objects.create(
            code = message.get("exec_id"),
            body=message
        )

    try:
        exec_request_mq = AMQP()
        exec_request_mq.basic_publish(message,"pytest.exec.report")
    except Exception as e:
        logger.error(f"Fail to publish message to execution engine,errors as following:{str(e)}.")

