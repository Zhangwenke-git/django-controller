# Generated by Django 3.2.8 on 2022-07-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiWhiteList',
            fields=[
                ('id', models.BigAutoField(help_text='Id', primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('url', models.CharField(help_text='url地址', max_length=200, verbose_name='url')),
                ('method', models.IntegerField(blank=True, default=0, help_text='接口请求方法', null=True, verbose_name='接口请求方法')),
                ('enable_datasource', models.BooleanField(blank=True, default=True, help_text='激活数据权限', verbose_name='激活数据权限')),
            ],
            options={
                'verbose_name': '接口白名单',
                'verbose_name_plural': '接口白名单',
                'db_table': 'api_white_list',
                'ordering': ('-create_datetime',),
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0, verbose_name='数据库类型')),
                ('host', models.CharField(max_length=64, verbose_name='服务器地址')),
                ('username', models.CharField(max_length=64, verbose_name='登录用户')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('dbname', models.CharField(max_length=64, verbose_name='数据库')),
                ('port', models.IntegerField(default=3306, verbose_name='端口')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name_plural': '数据库配置信息',
                'db_table': 'database',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='FTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=64, verbose_name='服务器地址')),
                ('username', models.CharField(max_length=64, verbose_name='登录用户')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('port', models.IntegerField(default=21, verbose_name='端口')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name_plural': 'FTP配置信息',
                'db_table': 'ftp',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.BigAutoField(help_text='Id', primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('request_modular', models.CharField(blank=True, help_text='请求模块', max_length=64, null=True, verbose_name='请求模块')),
                ('request_path', models.CharField(blank=True, help_text='请求地址', max_length=400, null=True, verbose_name='请求地址')),
                ('request_body', models.TextField(blank=True, help_text='请求参数', null=True, verbose_name='请求参数')),
                ('request_method', models.CharField(blank=True, help_text='请求方式', max_length=8, null=True, verbose_name='请求方式')),
                ('request_msg', models.TextField(blank=True, help_text='操作说明', null=True, verbose_name='操作说明')),
                ('request_ip', models.CharField(blank=True, help_text='请求ip地址', max_length=32, null=True, verbose_name='请求ip地址')),
                ('request_browser', models.CharField(blank=True, help_text='请求浏览器', max_length=64, null=True, verbose_name='请求浏览器')),
                ('response_code', models.CharField(blank=True, help_text='响应状态码', max_length=32, null=True, verbose_name='响应状态码')),
                ('request_os', models.CharField(blank=True, help_text='操作系统', max_length=64, null=True, verbose_name='操作系统')),
                ('json_result', models.TextField(blank=True, help_text='返回信息', null=True, verbose_name='返回信息')),
                ('status', models.BooleanField(default=False, help_text='响应状态', verbose_name='响应状态')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
                'db_table': 'system_operation_log',
                'ordering': ('-create_datetime',),
            },
        ),
        migrations.CreateModel(
            name='RabbitMQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=64, verbose_name='服务器地址')),
                ('username', models.CharField(max_length=64, verbose_name='登录用户')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('vhost', models.CharField(max_length=64, null=True, verbose_name='vhost')),
                ('exchange', models.CharField(max_length=128, null=True, verbose_name='交换机')),
                ('producer', models.CharField(max_length=128, null=True, verbose_name='请求队列')),
                ('consumer', models.CharField(max_length=128, null=True, verbose_name='消费队列')),
                ('port', models.IntegerField(default=5672, verbose_name='端口')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name_plural': 'MQ配置信息',
                'db_table': 'rabbitmq',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='Redis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=64, verbose_name='服务器地址')),
                ('username', models.CharField(max_length=64, verbose_name='登录用户')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('port', models.IntegerField(default=6379, verbose_name='端口')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name_plural': 'REDIS配置信息',
                'db_table': 'redis',
                'ordering': ('-create_time',),
            },
        ),
    ]
