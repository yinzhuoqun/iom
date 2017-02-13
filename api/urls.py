#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)


from django.conf.urls import include, url
from api.views import *



urlpatterns = [
    url(r"list", list),
    url(r"savedata", savedata),
]
