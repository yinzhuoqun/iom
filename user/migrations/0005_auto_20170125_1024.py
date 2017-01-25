# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170123_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('group_id', models.IntegerField(verbose_name='组 ID')),
                ('permission_id', models.IntegerField(verbose_name='权限 ID')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content_type_id', models.IntegerField(verbose_name='权限 ID')),
                ('codename', models.CharField(verbose_name='权限编码', max_length=32)),
                ('name', models.CharField(verbose_name='权限名称', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_id', models.IntegerField(verbose_name='用户 ID')),
                ('permission_id', models.IntegerField(verbose_name='权限 ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.AlterField(
            model_name='users',
            name='user_avatar',
            field=models.ImageField(null=True, verbose_name='用户头像', blank=True, upload_to='upload/user_avatar'),
        ),
    ]
