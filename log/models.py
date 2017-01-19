from django.db import models


# Create your models here.

class Log(models.Model):
    user = models.CharField(max_length=32, verbose_name="用户名称")
    time = models.DateTimeField(verbose_name="日志时间")
    operation = models.CharField(max_length=128, verbose_name="操作")
    level = models.IntegerField(verbose_name="日志等级")
    type = models.CharField(max_length=32, verbose_name="日志类型")
