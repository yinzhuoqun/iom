# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170122_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_online',
            field=models.CharField(default='OFF', verbose_name='在线状态', max_length=32),
        ),
    ]
