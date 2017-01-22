# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20170123_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='mac',
            field=models.CharField(verbose_name='MAC', max_length=32),
        ),
    ]
