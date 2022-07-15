# Generated by Django 3.2.8 on 2022-07-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期'),
        ),
        migrations.AddField(
            model_name='role',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日期'),
        ),
    ]