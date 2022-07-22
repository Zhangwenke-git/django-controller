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
    path('re-execute/',views.re_execute),
    path('batch-execute/',views.batch_execute),
    re_path(r'^report-download/(?P<pk>\w+)/$',views.report_download),
    re_path(r'^stop-task/(?P<pk>\w+)/$',views.stop_task),
    re_path(r'^delete-task/(?P<pk>\w+)/$',views.delete_task),
    re_path(r'^restore-task/(?P<pk>\w+)/$',views.restore_task),
    path('report-details/view/',views.report_view),
    path('parameter-fields/',views.parameter_fields),
    path('one-key-expression/',views.oneKeyExpression),
    path('process-parameterized/',views.process_parameterized_fields),
    path('send/request/',views.process_request),
    re_path(r'^make/request/(?P<pk>\w+)/$',views.make_request),
]

urlpatterns += router.urls
