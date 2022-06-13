from django.contrib import admin

# Register your models here.
from api.models import Project,TestSuit,TestCase,Templates,Scenario
admin.site.register(Project)
admin.site.register(TestSuit)
admin.site.register(TestCase)
admin.site.register(Templates)
admin.site.register(Scenario)
