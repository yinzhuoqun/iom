from django.db import models

# Create your models here.

class Server(models.Model):
    host = models.CharField(max_length=128,verbose_name="主机名称")
    ip = models.CharField(max_length=32,verbose_name="主机ip")
    mac = models.CharField(max_length=32,verbose_name="mac")
    cpu = models.CharField(max_length=32,verbose_name="cpu")
    mem = models.CharField(max_length=32,verbose_name="内存")
    disk = models.CharField(max_length=32,verbose_name="磁盘")
    system = models.CharField(max_length=32,verbose_name="系统")
    model = models.CharField(max_length=32,verbose_name="服务器型号")