import datetime

from django.db import models
from django.forms import Field


class Customer(models.Model):
    """
    客户表
    """
    pass


class Menu(models.Model):
    menu_type_choice = (
        (0, '菜单'),
        (1, '按钮')
    )
    menu_name = models.CharField(max_length=64, verbose_name='菜单名称')
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    menu_type = models.IntegerField(choices=menu_type_choice, verbose_name='菜单类型')
    menu_icon = models.CharField(max_length=128, verbose_name='记录icon名称')
    menu_order_num = models.IntegerField(verbose_name='排序字段', unique=True)
    menu_url = models.CharField(max_length=256, verbose_name='路由名称')

    def __str__(self):
        return f'{self.menu_name}'


class Permission(models.Model):
    permission_name = models.CharField(max_length=128, verbose_name='权限名称')
    router_url = models.CharField(max_length=128, verbose_name='路由地址')
    parent_permission = models.ForeignKey('self', on_delete=models.CASCADE)
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
    role_desc = models.CharField(max_length=256, verbose_name='角色描述')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now())

    def __str__(self):
        return self.get_identity_display()


class Department(models.Model):
    dep_name = models.CharField(max_length=64, verbose_name='部门名称')
    create_time = models.DateTimeField(default=datetime.datetime.now(), auto_now=True, verbose_name='创建时间')
    parent_dep = models.ForeignKey('self', on_delete=models.CASCADE)
    order_num = models.IntegerField(verbose_name='排序字段')

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
