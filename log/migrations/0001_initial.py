# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user', models.CharField(verbose_name='用户名称', max_length=32)),
                ('time', models.DateTimeField(verbose_name='日志时间')),
                ('operation', models.CharField(verbose_name='操作记录', max_length=128)),
                ('level', models.IntegerField(verbose_name='日志等级')),
                ('type', models.CharField(verbose_name='日志类型', max_length=32)),
            ],
        ),
    ]
