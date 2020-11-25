import datetime

from django.db import models
from django.forms import Field


class Permission(models.Model):

    permission_name = models.CharField(max_length=128, verbose_name='权限名称')
    router_url = models.CharField(max_length=128, verbose_name='路由地址')
    parent_permission = models.ForeignKey('self')


class Role(models.Model):
    identity_tuple = (
        (0, '管理员'),
        (1, '测试'),
        (2, '普通用户')

    )
    identity = models.IntegerField(choices=identity_tuple, verbose_name='用户角色')
    role_desc = models.CharField(max_length=256, verbose_name='角色描述')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now())

    def __str__(self):
        return self.get_identity_display()

class Department(models.Model):
    pass

class User(models.Model):
    gender_choice = (
        (0, '男性'),
        (1, '女性')
    )
    use_status = (
        (0,'不可用'),
        (1, '可用')
    )

    username = models.CharField(max_length=128, verbose_name='用户名称', db_index=True)
    email = models.CharField(max_length=64, verbose_name='用户邮箱')

    gender = models.SmallIntegerField(choices=gender_choice, verbose_name='性别')
    create_time = models.DateTimeField(verbose_name='创建时间', db_index=True)
    last_login_time = models.DateTimeField(verbose_name='最后登录时间', db_index=True)
    personal_desc = models.CharField(max_length=256, verbose_name='个人描述')
    phone_number = models.CharField(max_length=32, verbose_name='电话号码')
    use_status = models.SmallIntegerField(choices=use_status, verbose_name='用户状态')
    last_update_time = models.DateTimeField(verbose_name='修改时间', db_index=True)
    avatar = models.ImageField()
    # 角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # 部门
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}:{self.gender}:{self.use_status}"
