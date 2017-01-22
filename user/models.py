#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from django.db import models

# Create your models here.



class Users(models.Model):
    # unique 如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
    user_name = models.CharField(max_length=32, unique=True, verbose_name='用户名称')
    user_password = models.CharField(max_length=32, verbose_name='用户密码')
    user_email = models.EmailField(max_length=254, verbose_name='用户邮箱')
    user_phone = models.CharField(max_length=18, verbose_name='用户手机',
                                  blank=True, null=True)
    user_photo = models.ImageField(upload_to='images/user_photo', verbose_name='用户头像',
                                   blank=True, null=True)

    # DateField.auto_now_add 当对象第一次被创建时自动设置当前时间。用于创建时间的时间戳. 它总是使用当前日期；和你可以覆盖的那种默认值不一样。
    user_data_joined = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # DateField.auto_now 每次保存对象时，自动设置该字段为当前时间。用于"最后一次修改"的时间戳。注意，它总是使用当前日期；它不只是一个默认值，你可以覆盖。
    user_last_login = models.DateTimeField(auto_now=True, verbose_name='最近登录')
    # auto_now_add, auto_now, and default 这些设置是相互排斥的. 他们之间的任何组合将会发生错误的结果.
    user_online = models.CharField(max_length=32, default="OFF", verbose_name='在线状态')


class Groups(models.Model):
    user_group = models.CharField(max_length=32, verbose_name='用户组')


class Roles(models.Model):
    name = models.CharField(max_length=32, verbose_name="权限")

