# Generated by Django 3.2.8 on 2022-07-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_executionrecord_cron_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='default',
            field=models.JSONField(null=True, verbose_name='参数默认值'),
        ),
        migrations.AddIndex(
            model_name='crontabexecid',
            index=models.Index(fields=['code'], name='api_crontab_code_6d438e_idx'),
        ),
        migrations.AddIndex(
            model_name='executionrecord',
            index=models.Index(fields=['code'], name='api_executi_code_015b30_idx'),
        ),
        migrations.AddIndex(
            model_name='executionrequestbackup',
            index=models.Index(fields=['code'], name='api_executi_code_40bae5_idx'),
        ),
        migrations.AddIndex(
            model_name='scenario',
            index=models.Index(fields=['scenario'], name='api_scenari_scenari_1e915d_idx'),
        ),
        migrations.AddIndex(
            model_name='templates',
            index=models.Index(fields=['name'], name='api_templat_name_3c2472_idx'),
        ),
        migrations.AddIndex(
            model_name='testcase',
            index=models.Index(fields=['case'], name='api_testcas_case_97d46b_idx'),
        ),
    ]