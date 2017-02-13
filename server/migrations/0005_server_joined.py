# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20170123_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 22, 18, 10, 46, 507519, tzinfo=utc), verbose_name='采样时间', auto_now_add=True),
            preserve_default=False,
        ),
    ]
