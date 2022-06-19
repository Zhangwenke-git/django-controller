"""DjangoVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
import api.urls as api_urls
import user.urls as user_urls
# from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('user/', include(user_urls)),
    # path('docs/', include_docs_urls(title='站点页面标题'))
]


"""将jobs.py中的定时任务导入在该文件中，则python启动的时候则调用，使用apscheduler时需要导入该包"""
# from sse.lib.celery_job.celery_job import scheduler
