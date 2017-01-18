#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)

from django.shortcuts import render


# Create your views here.


def index(request):
    index_info = {"title_name": '智能运维平台', 'title_name_en': 'Intelligence Operation and Maintenance'}

    return render(request, "index.html", locals()) #  locals() 要传字典
    # return render_to_response("index.html", locals())

def blank(request):
    return render(request, "blank.html", locals())


def login(request):
    return render(request, "login.html", locals())


def froms(request):
    return render(request, "forms.html", locals())

def tables(request):
    return render(request, "tables.html", locals())

def flot(request):
    return render(request, "flot.html", locals())

def morris(request):
    return render(request, "morris.html", locals())

def base(request):
    index_info = {"title_name": '智能运维平台', 'title_name_en': 'Intelligence Operation and Maintenance'}
    return render(request, "base.html", locals())

def buttons(request):
    return render(request, "buttons.html", locals())

def icons(request):
    return render(request, "icons.html", locals())

def panels_wells(request):
    return render(request, "panels-wells.html", locals())

def typography(request):
    return render(request, "typography.html", locals())

def grid(request):
    return render(request, "grid.html", locals())

def notificions(request):
    return render(request, "notifications.html", locals())



