# Generated by Django 3.2.10 on 2022-07-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='executionrecord',
            name='cron_task_status',
            field=models.SmallIntegerField(choices=[(0, '未启动'), (1, '运行中'), (2, '已结束'), (3, '暂停'), (4, '已删除'), (5, '过期')], default=0, verbose_name='类型'),
        ),
    ]
