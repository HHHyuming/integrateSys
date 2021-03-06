# Generated by Django 3.1.3 on 2020-11-27 06:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0002_auto_20201127_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 14, 30, 20, 96384), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 27, 14, 30, 20, 97405), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_center.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 27, 14, 30, 20, 97405), verbose_name='最后登录时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_update_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 27, 14, 30, 20, 97405), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_center.role'),
        ),
    ]
