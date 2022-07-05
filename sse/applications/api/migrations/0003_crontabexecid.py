# Generated by Django 3.2.8 on 2022-07-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_executionrecord_cron_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrontabExecID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, null=True, verbose_name='执行编码')),
                ('task', models.CharField(max_length=64, null=True, verbose_name='定时任务名称')),
                ('task_type', models.SmallIntegerField(choices=[(0, '普通任务'), (1, '定时任务'), (2, '轮询任务')], null=True, verbose_name='任务类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '定时任务和执行编码对照表',
                'ordering': ('-create_time',),
            },
        ),
    ]
