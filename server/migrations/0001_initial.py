# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('host', models.CharField(verbose_name='主机名称', max_length=128)),
                ('ip', models.CharField(verbose_name='IP', max_length=32)),
                ('mac', models.CharField(verbose_name='MAC', max_length=32)),
                ('cpu', models.CharField(verbose_name='CPU', max_length=32)),
                ('mem', models.CharField(verbose_name='内存', max_length=32)),
                ('disk', models.CharField(verbose_name='磁盘', max_length=32)),
                ('system', models.CharField(verbose_name='系统', max_length=32)),
                ('model', models.CharField(verbose_name='服务器型号', max_length=32)),
            ],
        ),
    ]
