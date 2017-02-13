# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_users_user_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='users',
            name='user_avatar',
            field=models.ImageField(verbose_name='用户头像', upload_to='media/upload/user_avatar', null=True, blank=True),
        ),
    ]
