"""
添加定时器任务

"""
import time
import os, sys
import redis
import datetime
import json
import threading
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from sse.lib.utils.config_parser import ConfigParser
from api.models import ExecutionRecord,CrontabExecID
from sse.lib.core.cron_task import *
from sse.lib.core.period_task import *
from apscheduler.schedulers import SchedulerNotRunningError
from sse.lib.utils.logger import logger
from celery import shared_task
from django_celery_beat.models import PeriodicTask

logger = logger()

BASE_DIR = Path(__file__).resolve().parent.parent

redis_info = ConfigParser().getRedis

rds = redis.Redis(**redis_info, decode_responses=True)
"""
===================================使用apscheduler做定时任务===================================

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

try:
    @register_job(scheduler, "interval", seconds=ConfigParser().read_clean_report_internal, replace_existing=True)
    def clean_reports_job():
        try:
            logger.info(f"Start to clean reports under '/templates/ant' folder.")
            reports = os.path.join(BASE_DIR, r'templates\ant')
            for root, dirs, files in os.walk(reports):
                for file in files:
                    if file.endswith(".html") or file.endswith(".xml"):
                        delete_file = os.path.join(root, file)
                        os.remove(delete_file)
        except Exception as e:
            logger.error(f'Fail to remove report html file,error as following:{str(e)}')
        else:
            logger.debug(f'Success to remove report html file.')

    @register_job(scheduler, "cron",day_of_week="mon-sun", hour=ConfigParser().read_update_report_point, replace_existing=True)
    def update_expired_job():
        try:
            logger.debug(f"Start to update some records in execution_record table,whose status is executing-status and create time is over past 24 hours.")
            past_24_point = datetime.datetime.now()-datetime.timedelta(days=1)
            ExecutionRecord.objects.filter(statue=1,create_time__lt=past_24_point).update(statue=2)
        except Exception as e:
            logger.error(f"Fail to execute update_expired_job,error as following:{str(e)}.")

    scheduler.start()

except Exception as e:
    logger.error(f"Fail to execute reports-clean-job,error as following:{str(e)}.")
    try:
        scheduler.shutdown()
    except SchedulerNotRunningError:
         pass
         
==========================================结束===========================================
"""


@shared_task
def heart_beats():
    logger.info('*********************A heart beats message to check normal environments*********************')


@shared_task
def clean_reports_job():
    """
    每2小时清除一下templates/ant中的报告
    """
    try:
        logger.info(f"Start to clean reports under '/templates/ant' folder.")
        reports = os.path.join(BASE_DIR, r'templates\ant')
        for root, dirs, files in os.walk(reports):
            for file in files:
                if file.endswith(".html") or file.endswith(".xml"):
                    delete_file = os.path.join(root, file)
                    os.remove(delete_file)
    except Exception as e:
        logger.error(f'Fail to remove report html file,error as following:{str(e)}.')
    else:
        logger.info(f'Remove report html file successfully.')


@shared_task
def update_expired_job():
    """
    将execution_record表中执行状态超过24小时的数据置为超时状态，每天早上6点执行批处理
    @return:
    """
    try:
        logger.info(
            f"Start to update some records in execution_record table,whose status is executing-status and create time is over past 24 hours.")
        past_24_point = datetime.datetime.now() - datetime.timedelta(days=1)
        ExecutionRecord.objects.filter(statue=1, create_time__lt=past_24_point).update(statue=2)
    except Exception as e:
        logger.error(f"Fail to execute update_expired_job,error as following:{str(e)}.")
    else:
        logger.info(f'Update records successfully.')


@shared_task
def clean_logs_job(n):
    """
    清理生成的log文件
    """
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, r'logs')):
        for file in files:
            full_name = os.path.join(root, file)
            create_time = int(os.path.getctime(full_name))
            delta_days = (datetime.datetime.now() - datetime.timedelta(days=n))
            time_stamp = int(time.mktime(delta_days.timetuple()))
            if create_time < time_stamp:
                os.remove(full_name)


@shared_task
def clean_cron_task_job():
    """
    定时删除表中django_celery_beat_periodictask中的cron记录
    """
    cron_task_names = json.loads(rds.get("cron_task_names"))
    if len(cron_task_names) > 0:
        logger.info(f"Prepare to clean completed crontab: {cron_task_names}")
        try:
            # res = map(period_task_delete, cron_task_names)
            for cron in cron_task_names:
                period_task_delete(cron)
                crontab_obj = CrontabExecID.objects.get(task = cron)
                ExecutionRecord.objects.filter(code=crontab_obj.code).update(cron_task_status=4)
        except Exception as e:
            logger.error(f"Fail to clean completed crontab, due to error:{e}")
        else:
            rds.set("cron_task_names", json.dumps([]))
    else:
        logger.info("There are no completed crontab to clean.")


@shared_task
def reset_period_task_job():
    """
    定时更新表django_celery_beat_periodictask中的总跑次数大等于3的period记录
    """

    def reset_gte3_count(period_obj):
        period_obj.enabled = False
        period_obj.total_run_count = 0
        period_obj.save()

    periods = PeriodicTask.objects.filter(total_run_count__gte=2, name__contains='PERIOD')
    try:

        if len(periods) > 0:
            logger.info(f"Prepare to stop period tasks: {periods}.")
            for period in periods:
                reset_gte3_count(period)
                try:
                    crontab_obj = CrontabExecID.objects.get(task = period.name)
                    ExecutionRecord.objects.filter(code=crontab_obj.code).update(cron_task_status=3)
                except Exception:
                    pass
        else:
            logger.info(f"There are no period-records in table [django_celery_beat_periodictask] to be updated.")

    except Exception as e:
        logger.error(f"Update records in table [django_celery_beat_periodictask] failed,due to error:{str(e)}")
    else:
        if len(periods) > 0: logger.info(f"Update records in table [django_celery_beat_periodictask] successfully.")
