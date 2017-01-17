#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import os
import time

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='conf.log',
                    filemode='a+')

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# %(name)-12s:  -12 间距
formatter = logging.Formatter('%(name)s: %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-2s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

try:
    import configparser
except:
    import ConfigParser as configparser

lof_conf_name = 'log.conf'  # log 配置文件名称
section_log = "default"  # log 配置文件 section 的名称
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(lof_conf_name):
    config_file = os.path.join(BASE_DIR, lof_conf_name)
    conf = configparser.ConfigParser()
    conf.read(config_file)
    secs = conf.sections()
    logging.info(secs)
    # log_path = conf.get("default", "log_dir")
else:
    logging.error("%s 配置文件不存在" % lof_conf_name)


def mkdir_log_path(log_dir):
    """
    创建日志的目录，如果已存在则不需创建
    """
    if not os.path.isdir(log_dir):
        print("创建%s目录" % log_dir)
        os.makedirs(log_dir)


def logging_file_path(log_type):
    """按日志类别生成对应的日志文件的完整路径
    """
    if section_log in secs:
        logging.info("%s in secs is %s" % (section_log, True))
        # for opt in conf.options(section_log):
        #     print(opt)
        try:
            log = conf.get(section_log, log_type)
            logging.info('log %s' % log)
            log_path = os.path.join(BASE_DIR, log)
            logging.info('path %s' % log_path)
            if not os.path.exists(log_path):
                os.mkdir(log_path)
            return os.path.join(log_path, "%s.log" % log_type)
        except Exception as e:
            logging.error(e)

            # if log_type == "error":
            #     log_error = conf.get("default", "log_error")
            #     log_path = os.path.join(BASE_DIR, log_error)
            #     return os.path.join(log_path, "%s.log" % log_type)
            # elif log_type == "warning":
            #     log_warning = conf.get("default", "log_warning")
            #     log_path = os.path.join(BASE_DIR, log_warning)
            #     return os.path.join(log_path, "%s.log" % log_type)
            # elif log_type == "info":
            #     log_info = conf.get("default", "log_info")
            #     log_path = os.path.join(BASE_DIR, log_info)
            #     return os.path.join(log_path, "%s.log" % log_type)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'notes': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logging_file_path('all'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'default',
        },
        'success': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logging_file_path('success'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'default',
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logging_file_path('warning'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'default',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logging_file_path('error'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'loggers': {
        # 定义了一个logger
        'notice': {
            'level': 'DEBUG',
            'handlers': ['console', 'notes', 'success', 'warning', 'error', 'all'],
            'propagate': True
        }
    }
}

if __name__ == '__main__':
    # logging_file_path('info')
    pass
