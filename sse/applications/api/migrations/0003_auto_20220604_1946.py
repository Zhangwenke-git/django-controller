# Generated by Django 3.2.8 on 2022-06-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='parameter',
            field=models.JSONField(null=True, verbose_name='请求参数'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='validator',
            field=models.JSONField(null=True, verbose_name='验证字段'),
        ),
    ]