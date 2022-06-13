# -*-coding=utf-8-*-

import os
from datetime import datetime
import logging.config
from django.conf import settings
from sse.lib.utils.config_parser import ConfigParser

level = ConfigParser().print_level

# 定义三种日志输出格式 开始
# standard_format = '[%(asctime)s] [%(levelname)s] [%(threadName)s:%(thread)d] [%(name)s] [%(filename)s:%(lineno)d]' \
#                   ' %(message)s'  # 其中name为getLogger()指定的名字；lineno为调用日志输出函数的语句所在的代码行
standard_format = '[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(name)s] | %(message)s'  # 其中name为getLogger()指定的名字；lineno为调用日志输出函数的语句所在的代码行
simple_format = '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] | %(message)s'
id_simple_format = '[%(asctime)s] [%(levelname)s] | %(message)s'
# 定义日志输出格式 结束

logfile_dir = os.path.join(settings.BASE_DIR, 'logs')  # C:\Users\oldboy\Desktop\atm\log

logfile_name = 'log{0}.log'.format(datetime.now().strftime('%Y-%m-%d'))  # log文件名，需要自定义路径名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):  # C:\Users\oldboy\Desktop\atm\log
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)  # C:\Users\oldboy\Desktop\atm\log\log.log
# 定义日志路径 结束

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},  # filter可以不定义
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M  (*****)
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置。如果''设置为固定值logger1，则下次导入必须设置成logging.getLogger('logger1')
        '': {
            # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            #'handlers': ['default', 'console'],
            'handlers': ['default', 'console'],
            'level': level.upper(),
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}


def logger():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    return logger

