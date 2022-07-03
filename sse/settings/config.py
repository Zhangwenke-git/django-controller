import os
import datetime
from pathlib import Path
#AttributeError: 'WindowsPath' object has no attribute 'rstrip' 则删除BASE_DIR = Path(__file__).resolve().parent.parent的用法

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from sse.lib.utils.config_parser import ConfigParser

CONSTANT = ConfigParser()
# ================================================= #
# ******************* Restframework配置 ***********#
# ================================================= #


REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",  # 日期时间格式配置
    "DATE_FORMAT": "%Y-%m-%d",
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        # 'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/min',  # 未登录用户访问频率限制
        'user': '70/min',  # 登录用户访问频率限制
        'project_view': '30/min',  # 局部视图频率限制
        'user_view': '30/min',
    },

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # 认证组件
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 'EXCEPTION_HANDLER': 'sse.lib.core.exceptions.exc_exceptions',  # 自定义的异常捕获
    'EXCEPTION_HANDLER': 'sse.lib.core.exceptions.CustomExceptionHandler',  # 自定义的异常捕获
    'DEFAULT_FILTER_BACKENDS': (
        # 'django_filters.rest_framework.DjangoFilterBackend',
        'sse.lib.utils.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),  # 筛选组件
    # 'DEFAULT_PAGINATION_CLASS': 'CustomPagination',  # LimitOffsetPagination 分页风格
    'DEFAULT_PAGINATION_CLASS': 'sse.lib.utils.pagination.CustomPagination',  # LimitOffsetPagination 分页风格
    #'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',  # 生成API文档
}

JWT_AUTH = {
    "JWT_AUTH_HEADER_PREFIX": "",
    # "JWT_RESPONSE_PAYLOAD_HANDLER": "sse.lib.core.jwt_response_handler.jwt_response_handler",  # 自定义认证组件
    "JWT_RESPONSE_PAYLOAD_HANDLER": "sse.lib.core.jwt_response_handler.jwt_response_handler",  # 自定义认证组件
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # 超时组件
}

CORS_ALLOW_CREDENTIALS = True

IP_SCOPED = False

if not IP_SCOPED:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ORIGIN_WHITELIST = (
        'www.example.com',
    )

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'authorization',
    'content-type',
    'redirect',
    'origin',
    'user-agent',
    'x-csrftoken',
)

HEADER_CHECKER = False  # 使用自定义的token规则还是jwt_自带的规则




# ================================================= #
# ******************* Celery配置 ***********#
# ================================================= #


from celery import Celery, platforms

platforms.C_FORCE_ROOT = True

# launcher order
# 先启动项目 python manage.py runserver 9091后再执行异步任务命令
# python manage.py celery worker --loglevel=info


# python pip 安装报错 error in setup command: use_2to3 is invalid. 解决方法:pip install setuptools==57.5.0


# 最重要的配置，设置消息broker,格式为：db://user:password@host:port/dbname
# 如果redis安装在本机，使用localhost
# 如果docker部署的redis，使用redis://redis:6379
CELERY_BROKER_URL = "redis://192.168.44.129:6379/0"
# CELERY_BROKER_URL = "redis://192.168.246.128:6379/0"

# 使用rabbit数据库
# CELERY_BROKER_URL = "amqp://admin:aaaa1111!@192.168.44.129:5672//"


# celery时区设置，建议与Django settings中TIME_ZONE同样时区，防止时差
# Django设置时区需同时设置USE_TZ=True和TIME_ZONE = 'Asia/Shanghai'
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ENABLE_UTC = False
# 为django_celery_results存储Celery任务执行结果设置后台
# 格式为：db+scheme://user:password@host:port/dbname
# 支持数据库django-db和缓存django-cache存储任务状态及结果
CELERY_RESULT_BACKEND = "django-db"
# celery内容等消息的格式设置，默认json
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# 为任务设置超时时间，单位秒。超时即中止，执行下个任务。
CELERY_TASK_TIME_LIMIT = 5

# 任务限流
CELERY_TASK_ANNOTATIONS = {'sse.celery_job.lib.jobs.celery_exec_request': {'rate_limit': '10/s'}}

# Worker并发数量，一般默认CPU核数，可以不设置
CELERY_WORKER_CONCURRENCY = 20

# 每个worker执行了多少任务就会死掉，默认是无限的
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100

# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'  #可以进入Periodic Task表添加和修改周期性任务

CELERY_DISABLE_RATE_LIMITS = True


DJANGO_CELERY_BEAT_TZ_AWARE = False

# 非常重要,有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# ———————————启动步骤—————————————
# 1、启动python manage.py runserver 9091命令

# 2、启动Celery任务
# Windows下测试，启动Celery
# celery -A sse worker -l info -P eventlet

# 3、启动Celery定时任务命令
# celery -A sse beat -l info
# celery -A sse beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# 4、启动flower,浏览器打开，管理定时任务
# celery --broker=redis://192.168.44.129:6379/0 flower #启动flower监控页面








# ================================================= #
# ********************* 日志配置 ******************* #
# ================================================= #

# log 配置部分BEGIN #
SERVER_LOGS_FILE = os.path.join(BASE_DIR, "logs", "server.log")
ERROR_LOGS_FILE = os.path.join(BASE_DIR, "logs", "error.log")
if not os.path.exists(os.path.join(BASE_DIR, "logs")):
    os.makedirs(os.path.join(BASE_DIR, "logs"))

# 格式:[2020-04-22 23:33:01][micoservice.apps.ready():16] [INFO] 这是一条日志:
# 格式:[日期][模块.函数名称():行号] [级别] 信息
STANDARD_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
CONSOLE_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": STANDARD_LOG_FORMAT},
        "console": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": SERVER_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 5,  # 最多备份5个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ERROR_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 3,  # 最多备份3个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        # default日志
        "": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "scripts": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        # 数据库相关日志
        "django.db.backends": {
            "handlers": [],
            "propagate": True,
            "level": "INFO",
        },
    },
}
