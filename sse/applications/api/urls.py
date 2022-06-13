# from django.urls import path,re_path
# from api import views
# app_name='api'
#
# urlpatterns = [
#     # path('api_projects/',views.ApiprojectView.as_view()),
#     # re_path(r'^api_projects/(?P<pk>\d+)/$',views.ApiprojectDetailView.as_view()),
#     #
#     # path('testsuits/', views.TestSuitView.as_view()),
#     # re_path(r'^testsuits/(?P<pk>\d+)/$', views.TestSuitDetailView.as_view()),
#
# ]

from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from api import views
app_name='api'
# re_path(r'^(\w+)/(\w+)/(\d+)/check/$', api_view.check_template, name="check_template"),

router = SimpleRouter()
router.register('project',views.ProjectViewSet,'apiproject')
router.register('suit',views.TestSuitViewSet,'suit')
router.register('case',views.TestCaseViewSet,'case')
router.register('template',views.TemplateViewSet,'template')
router.register('scenario',views.ScenarioViewSet,'scenario')
router.register('report',views.ReportViewSet,'report')

urlpatterns = [
    path('execute/',views.execute),
    path('batch-execute/',views.batch_execute),
    path('report-details/view/',views.report_view),
    path('parameter-fields/',views.parameter_fields),
]

urlpatterns += router.urls
