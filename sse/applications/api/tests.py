from django.test import TestCase
import os
import datetime
# Create your tests here.
from api.models import Project,Scenario,Templates,TestCase,TestSuit,ExecutionRecord

if __name__ == "__main__":
    past_24_point = datetime.datetime.now() - datetime.timedelta(days=1)
    print(past_24_point)
    ExecutionRecord.objects.filter(statue=1, create_time__lt=past_24_point).update(statue=2)
