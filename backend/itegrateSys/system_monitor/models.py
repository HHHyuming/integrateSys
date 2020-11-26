from django.db import models


# Create your models here.
class SystemActionRecord(models.Model):
    operation_name = models.CharField(max_length=32, verbose_name='操作人')
    operation_desc = models.CharField(max_length=64, verbose_name='操作描述')
    operation_method = models.CharField(max_length=128, verbose_name='操作方法，function')
    operation_args = models.CharField(max_length=128, verbose_name='方法参数')
    operation_ip = models.CharField(max_length=16, verbose_name='操作IP地址')
    operation_addr = models.CharField(max_length=512, verbose_name='操作地点')
    operation_datetime = models.DateTimeField(auto_now=True)
    consume_time = models.IntegerField(verbose_name='耗时')


class UserLoginRecord(models.Model):
    user_name = models.CharField(max_length=16, verbose_name='用户名')
    login_platform = models.CharField(max_length=32, verbose_name='登录平台')
    browser_version = models.CharField(max_length=16, verbose_name='浏览器')
    login_ip = models.CharField(max_length=16, verbose_name='登录IP')
    login_addr = models.CharField(max_length=512, verbose_name='登录地点')
    login_datetime = models.DateTimeField(auto_now=True)
