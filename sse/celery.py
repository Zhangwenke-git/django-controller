from __future__ import absolute_import, unicode_literals
"""
Celery的初始化
"""


import os,sys
from celery import Celery
from sse.lib.utils.config_parser import ConfigParser
from celery.schedules import crontab
from datetime import timedelta



# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sse.settings.dev')

# 实例化，需要改成自己的项目名称
app = Celery('sse')

# namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动从Django的指定的位置中发现任务
app.autodiscover_tasks(packages=['sse.celery_job'])

# 自动从Django的指定的包中发现定时任务
app.conf['imports'] = ['sse.celery_job.jobs',]



# 一个测试任务,测试celery环境是否正常，出现[2022-05-24 12:01:41,008: INFO/MainProcess] celery@Zhangwenke ready.则说明正常
@app.task(bind=True)
def debug_test_task(self):
    print(f'Request: {self.request!r}')



app.conf.update(
    CELERYBEAT_SCHEDULE={
        'heart_beats_job': {
            'task': 'sse.celery_job.jobs.heart_beats',
            'schedule': timedelta(seconds=60),
            'args': ()
        },
        'clean_logs_job': {
            'task': 'sse.celery_job.jobs.clean_logs_job',
            'schedule': crontab(hour=5, minute=30),
            'args': (7,)
        },
        'clean_reports_job': {
            'task': 'sse.celery_job.jobs.clean_reports_job',
            'schedule': timedelta(seconds=7200),
            'args': ()
        },
        'update_expired_job': {
            'task': 'jobs.update_expired_job',
            'schedule': crontab(hour=6, minute=0),
            'args': ()
        }
    }
)

