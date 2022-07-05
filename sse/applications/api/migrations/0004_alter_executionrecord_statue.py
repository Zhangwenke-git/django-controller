# Generated by Django 3.2.8 on 2022-07-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_crontabexecid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executionrecord',
            name='statue',
            field=models.SmallIntegerField(choices=[(0, '执行完毕'), (1, '执行中'), (2, '执行超时'), (3, '执行异常'), (4, '未启动')], default=4, verbose_name='状态'),
        ),
    ]