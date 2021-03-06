# Generated by Django 3.2.8 on 2022-06-19 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuit',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='testsuit',
            name='project',
            field=models.ManyToManyField(to='api.Project', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.templates', verbose_name='模板'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='testsuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suit_case', to='api.testsuit', verbose_name='用例集合'),
        ),
        migrations.AddField(
            model_name='templates',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='sql',
            name='case',
            field=models.ManyToManyField(to='api.TestCase', verbose_name='所涉用例'),
        ),
        migrations.AddField(
            model_name='sql',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='cases',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_scenario', to='api.testcase', verbose_name='测试函数（用例）'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
    ]
