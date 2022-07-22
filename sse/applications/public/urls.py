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
from public import views
app_name='public'
# re_path(r'^(\w+)/(\w+)/(\d+)/check/$', api_view.check_template, name="check_template"),

from rest_framework_bulk.routes import BulkRouter

bulk_router = BulkRouter()
#router = SimpleRouter()


bulk_router.register(r'db',views.DatabaseViewSet)
bulk_router.register(r'redis',views.RedisViewSet)
bulk_router.register(r'mq',views.RabbitMQViewSet)
bulk_router.register(r'ftp',views.FTPViewSet)


urlpatterns = [
]

urlpatterns += bulk_router.urls

