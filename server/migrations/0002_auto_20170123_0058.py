# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='cpu',
            field=models.CharField(verbose_name='CPU', max_length=128),
        ),
    ]
