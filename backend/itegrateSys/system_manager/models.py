from django.db import models

# Create your models here.

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
