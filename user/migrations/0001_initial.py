# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_group', models.CharField(max_length=32, verbose_name='用户组')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32, unique=True, verbose_name='用户名称')),
                ('user_password', models.CharField(max_length=32, verbose_name='用户密码')),
                ('user_email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('user_phone', models.CharField(blank=True, max_length=18, null=True, verbose_name='用户手机')),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='images/user_photo', verbose_name='用户头像')),
                ('user_data_joined', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_last_log', models.DateTimeField(auto_now=True, verbose_name='最近登录')),
            ],
        ),
    ]
