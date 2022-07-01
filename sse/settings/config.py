import os
import datetime
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from sse.lib.utils.config_parser import ConfigParser
CONSTANT = ConfigParser()
# ================================================= #
# ********************* Restframework配置 ******************* #
# ================================================= #


REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",  # 日期时间格式配置
    "DATE_FORMAT": "%Y-%m-%d",
'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        #'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/min', # 未登录用户访问频率限制
        'user': '70/min', # 登录用户访问频率限制
        'project_view': '30/min', # 局部视图频率限制
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
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',  # 生成API文档
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


HEADER_CHECKER=False  #使用自定义的token规则还是jwt_自带的规则

















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
