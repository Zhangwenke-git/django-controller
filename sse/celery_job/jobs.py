"""
添加定时器任务

"""
import time
import os,sys
import datetime
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from sse.lib.utils.config_parser import ConfigParser
from api.models import ExecutionRecord
from apscheduler.schedulers import SchedulerNotRunningError
from sse.lib.utils.logger import logger
from celery import shared_task

logger = logger()

BASE_DIR = Path(__file__).resolve().parent.parent
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
            full_name = os.path.join(root,file)
            create_time = int(os.path.getctime(full_name))
            delta_days = (datetime.datetime.now() - datetime.timedelta(days = n))
            time_stamp  = int(time.mktime(delta_days.timetuple()))
            if create_time < time_stamp:
                os.remove(full_name)
