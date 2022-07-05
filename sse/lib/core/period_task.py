import json
import uuid
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule



def interval_scheduler_create(interval):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=int(interval),
        period=IntervalSchedule.MINUTES,
     )
    return schedule


def period_task_create(interval,message,task_name=None,task='sse.celery_job.tasks.celery_exec_request',expired_time=60):
    if not task_name:
        task_name = "PERIOD"+str(uuid.uuid4()).replace("-","")
    if message:
        message=json.dumps([message,False],ensure_ascii=False)
    schedule = interval_scheduler_create(interval)
    PeriodicTask.objects.create(
         interval=schedule,
         name=task_name,
         task=task,
         args=message,
         expires=datetime.now() + timedelta(seconds=int(expired_time)) # 任务的执行超时时间，避免任务执行时间过长
    )
    return task_name



def period_task_delete(task_name):
    PeriodicTask.objects.get(name=task_name).delete()


def period_task_stop(task_name):
    obj = PeriodicTask.objects.get(name=task_name)
    if obj.enabled:
         obj.enabled= False
         obj.save()

def period_task_restore(task_name):
    obj = PeriodicTask.objects.get(name=task_name)
    if not obj.enabled:
         obj.enabled= True
         obj.save()

