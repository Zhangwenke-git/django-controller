import pytz
import json
import uuid
from datetime import datetime, timedelta
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import PeriodicTask

def date_str_parser(string):
    current_year = datetime.now().year
    formatter = ['%Y-%m-%d %H:%M:%S','%Y/%m/%d %H:%M:%S']
    date_ = None
    try:
        for f in formatter:
            try:
                date_ = datetime.strptime(string, f)
            except Exception:
                raise NotImplementedError("Formatter error.")
            else:
                break
    except:
        raise ValueError("Only support date formatter: %Y-%m-%d %H:%M:%S and '%Y/%m/%d %H:%M:%S'")
    else:
        if date_:
            if date_.year == current_year:
                return date_.year,date_.month,date_.day, date_.hour,date_.minute,date_.second


def cron_scheduler_create(expression):
    schedule = None
    data = date_str_parser(expression)
    if data:
        y,m,d,h,m_,s = data
    # else:
    #     y,m,d,h,m_ = '*','*','*','*','*'
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=str(m_),
            hour=str(h),
            day_of_week='*',
            day_of_month=str(d),
            month_of_year=str(m),
            timezone=pytz.timezone('Asia/Shanghai')
        )
    return schedule


def cron_task_create(expression, message=None,task_name=None, task='sse.celery_job.tasks.celery_exec_request', expired_time=60):
    if not task_name:
        task_name = "CRON"+str(uuid.uuid4()).replace("-","")
    if message:
        message=json.dumps([message,False],ensure_ascii=False)
    schedule = cron_scheduler_create(expression)
    if schedule:
        PeriodicTask.objects.create(crontab=schedule, name=task_name, task=task,
                                    expires=datetime.now() + timedelta(seconds=int(expired_time)),
                                    args=message)
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
