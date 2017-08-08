#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from user.models import *
from user.forms import *
from server.models import *
import hashlib


# Create your views here.



def calc_md5(data, data1):
    """
    生成加盐密码函数
    """
    data = data.encode('utf-8')
    data1 = data1.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(data + b'yinzhuoqun' + data1)
    pw = md5.hexdigest()
    print(str(data) + ':' + '\'' + pw + '\'')
    return pw


def user_valid(username, passwd):
    try:
        user = Users.objects.get(user_name=username)
        print(user.user_password)
        print(calc_md5(username, passwd))
        if user.user_password == calc_md5(username, passwd):
            return True
        else:
            return False
    except:
        return False


def user_exists(username):
    try:
        Users.objects.get(user_name=username)
        return True
    except:
        return False


def login_valid(func):  # 这是一个装饰器的函数，外层的函数是用来接收被装饰函数的的
    def inner(request, *args, **kwargs):
        try:
            username = request.session["username"]  # 尝试获取session
            return func(request)  # index(request) 如果获取到执行被装饰函数
        except KeyError as e:  # 否则返回404页面
            if repr(e) == "KeyError('username',)":
                err = "当前用户未登录请登录"
            else:
                err = str(e)

            url = "/404/%s" % err
            # url = "/404/"
            # url ='/404/username'
            print(url)
            # url = "/404?err="+err
            # /404/当前用户未登录，请登录
            return HttpResponseRedirect('/login')

    return inner


# repr 是将类当中魔术方法__repr__的结果返回回来


@login_valid  # index = login_valid(index)  # login_valid(index) = inner  #index = inner
def index(request):
    statue = "Home | IOM"
    users_total = len(Users.objects.all())
    servers_total = len(Server.objects.all())
    return render(request, "index.html", locals())


# @login_valid
def test(request):
    user = user_exists("while")
    user_1 = user_valid("whileb", "whileb")
    # username = request.session["username"]
    req = dir(request)
    return render_to_response("test.html", locals())


# @login_valid
def register(request):
    # 清除登录记录
    try:
        del request.COOKIES["username"]
    except Exception as e:
        pass
    try:
        del request.session["username"]
    except Exception as e:
        pass

    statue = "用户注册"
    if request.method == "POST" and request.POST:
        # 数据中有图像字段，因此实例化Form类时，要加上第2个参数requst.FILES。
        registerFrom = RegisterForm(request.POST, request.FILES)  # registerFrom 网页变量
        # print(registerFrom.is_valid())
        if registerFrom.is_valid():
            clear_data = registerFrom.cleaned_data
            # print(clear_data.get("'user_name'"), clear_data.get("user_password"))
            print(clear_data.get("user_avatar"))
            # 存数据库
            u_info = Users(
                user_name=clear_data.get('user_name').strip(),  # 第一个user_name是数据库的字段名称，第二个user_name是表单的名称获取页面变量的值
                user_password=calc_md5(clear_data.get("user_name"), clear_data.get("user_password")),
                user_email=clear_data.get("user_email").strip(),
                user_phone=clear_data.get("user_phone").strip(),
                user_avatar=clear_data.get("user_avatar")
            )
            print(u_info.user_avatar)
            u_info.save()
            # del request.COOKIES["username"]
            # del request.session["username"]
            return HttpResponseRedirect("/login")
    else:
        registerFrom = RegisterForm()

    return render(request, "register.html", locals())


def logout(request):
    # print(request.method)
    # print(dir(request.GET))
    # if request.method == "GET" and request.GET:
    if request.method == "GET":
        username = request.session.get("username")
        # username = request.GET.get("username", "").strip()
        print('name:', username)

        # 退出的时候标记在线状态为 OFF
        user = Users.objects.get(user_name=username)
        user.user_online = "OFF"
        # print(user)
        user.save()

    try:
        del request.COOKIES["username"]
    except Exception as e:
        pass
    try:
        del request.session["username"]
    except Exception as e:
        pass

    return render_to_response("logout.html",locals())


def login(request):
    result = {}
    if request.method == "POST" and request.POST:
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        # print(username)
        # print(password)
        # print(user_valid(username, password))
        if username and password and user_valid(username, password):
            response = HttpResponseRedirect("/index")
            response.set_cookie("username", username)
            request.session["username"] = username
            # return response

            # 登陆的时候标记在线状态为 ON
            user = Users.objects.get(user_name=username)  # .update(user_online="ON")
            user.user_online = "ON"
            # print(user)
            user.save()
            return render(request, "index.html", locals())
        else:
            result["error"] = "用户名或密码错误"
            return render(request, "login.html", locals())
    else:
        return render(request, "login.html", locals())


def users(request):
    user = Users.objects.all()
    statue = "用户列表"
    location = "用户信息 > 用户列表"
    return render_to_response("users.html", locals())


def notfound(request, error):
    return render_to_response("404.html", locals())


def groups(request):
    group = Groups.objects.all()
    statue = "用户组"
    title = "Groups"
    projectname = "IOM"
    location = "用户组信息 > 用户组"
    return render(request, 'groups.html', locals())


def userpermission(request):
    userp = UserPermission.objects.all()
    statue = "用户权限"
    title = "UserPermission"
    projectname = "IOM"
    location = "用户信息 > 用户权限"
    return render(request, 'user_permission.html', locals())


def grouppermission(request):
    groupp = GroupPermission.objects.all()
    statue = "用户组权限"
    title = "GroupPermission"
    projectname = "IOM"
    location = "用户组信息 > 用户组权限"
    return render(request, 'group_permission.html', locals())

def permission(request):
    perm = Permission.objects.all()
    statue = "权限"
    title = "Permission"
    projectname = "IOM"
    location = "用户信息 > 权限"
    return render(request, 'permission.html', locals())


def list(request):
    statue = "列表展示页"
    table_list = [
        {
            "host": "bian-PC",
            "ip": "192.168.0.204",
            "system": "redhat7",
            "online": "是",
            "model": "联想System x3850"
        },
        {
            "host": "while-PC",
            "ip": "192.168.0.106",
            "system": "Windows7",
            "online": "否",
            "model": "HPE DL380 Gen9"
        },
    ]
    return render_to_response("servers.html", locals())


#
# def index(request):
#     index_info = {"title_name": '智能运维平台', 'title_name_en': 'Intelligence Operation and Maintenance'}
#
#     return render(request, "index.html", locals())  # locals() 要传字典
#     # return render_to_response("index.html", locals())


def blank(request):
    return render(request, "blank.html", locals())


#
# def login(request):
#     return render(request, "login.html", locals())


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
