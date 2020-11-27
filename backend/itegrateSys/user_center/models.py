import datetime


from django.utils import timezone
from django.db import models


class Permission(models.Model):
    permission_name = models.CharField(max_length=128, verbose_name='权限名称')
    router_url = models.CharField(max_length=128, verbose_name='路由地址', null=True)
    parent_permission = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='父级权限', null=True)
    # 角色权限多对多
    role = models.ManyToManyField('Role')

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __str__(self):
        return f'{self.permission_name}:{self.router_url}'


class Role(models.Model):
    identity_tuple = (
        (0, '管理员'),
        (1, '测试'),
        (2, '普通用户')

    )
    identity = models.IntegerField(choices=identity_tuple, verbose_name='用户角色')
    role_desc = models.CharField(max_length=256, verbose_name='角色描述', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    def __str__(self):
        return self.get_identity_display()


class Department(models.Model):
    dep_name = models.CharField(max_length=64, verbose_name='部门名称')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    parent_dep = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    order_num = models.IntegerField(verbose_name='排序字段', null=True)

    def __str__(self):
        return f'{self.dep_name}:{self.create_time}'


class User(models.Model):
    gender_choice = (
        (0, '男性'),
        (1, '女性')
    )
    use_status = (
        (0, '不可用'),
        (1, '可用')
    )

    username = models.CharField(max_length=128, verbose_name='用户名称', db_index=True)
    password = models.CharField(max_length=128, verbose_name='用户密码',blank=True)
    email = models.CharField(max_length=64, verbose_name='用户邮箱', null=True)

    gender = models.SmallIntegerField(choices=gender_choice, verbose_name='性别', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', db_index=True, default=timezone.now)
    last_login_time = models.DateTimeField(verbose_name='最后登录时间', db_index=True, default=timezone.now)
    personal_desc = models.CharField(max_length=256, verbose_name='个人描述', null=True)
    phone_number = models.CharField(max_length=32, verbose_name='电话号码', null=True)
    use_status = models.SmallIntegerField(choices=use_status, verbose_name='用户状态', null=True)
    last_update_time = models.DateTimeField(verbose_name='修改时间', db_index=True,default=timezone.now)
    avatar = models.CharField(max_length=512, verbose_name='图片地址', null=True)
    # 角色
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    # 部门
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.username}:{self.gender}:{self.use_status}"
