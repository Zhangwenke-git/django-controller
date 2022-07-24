from django.conf import settings
from django.db import models

table_prefix = settings.TABLE_PREFIX


class CoreModel(models.Model):
    """
    核心标准抽象模型模型,可直接继承使用
    增加审计字段, 覆盖字段时, 字段名称请勿修改, 必须统一审计字段名称
    """
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    description = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    update_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间")
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                           verbose_name="创建时间")

    class Meta:
        abstract = True


class OperationLog(CoreModel):
    request_modular = models.CharField(max_length=64, verbose_name="请求模块", null=True, blank=True, help_text="请求模块")
    request_path = models.CharField(max_length=400, verbose_name="请求地址", null=True, blank=True, help_text="请求地址")
    request_body = models.TextField(verbose_name="请求参数", null=True, blank=True, help_text="请求参数")
    request_method = models.CharField(max_length=8, verbose_name="请求方式", null=True, blank=True, help_text="请求方式")
    request_msg = models.TextField(verbose_name="操作说明", null=True, blank=True, help_text="操作说明")
    request_ip = models.CharField(max_length=32, verbose_name="请求ip地址", null=True, blank=True, help_text="请求ip地址")
    request_browser = models.CharField(max_length=64, verbose_name="请求浏览器", null=True, blank=True, help_text="请求浏览器")
    response_code = models.CharField(max_length=32, verbose_name="响应状态码", null=True, blank=True, help_text="响应状态码")
    request_os = models.CharField(max_length=64, verbose_name="操作系统", null=True, blank=True, help_text="操作系统")
    json_result = models.TextField(verbose_name="返回信息", null=True, blank=True, help_text="返回信息")
    status = models.BooleanField(default=False, verbose_name="响应状态", help_text="响应状态")

    class Meta:
        db_table = table_prefix + "system_operation_log"
        verbose_name = "操作日志"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)


class ApiWhiteList(CoreModel):
    url = models.CharField(max_length=200, help_text="url地址", verbose_name="url")
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.IntegerField(default=0, verbose_name="接口请求方法", null=True, blank=True, help_text="接口请求方法")
    enable_datasource = models.BooleanField(default=True, verbose_name="激活数据权限", help_text="激活数据权限", blank=True)

    class Meta:
        db_table = table_prefix + "api_white_list"
        verbose_name = "接口白名单"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)


class Database(models.Model):
    TYPE_CHOICES = (
        (0, "MYSQL"),
        (1, "ORACLE"),
    )
    type = models.IntegerField(default=0, verbose_name="数据库类型")
    name = models.CharField(max_length=128,unique=True,verbose_name="备注信息")
    host = models.CharField(max_length=64, verbose_name="服务器地址")
    username = models.CharField(max_length=64, verbose_name="登录用户")
    password = models.CharField(max_length=64,null=True, verbose_name="密码")
    dbname = models.CharField(max_length=64, verbose_name="数据库")
    port = models.IntegerField(default=3306, verbose_name="端口")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    class Meta:
        db_table = table_prefix + "database"
        verbose_name_plural = "数据库配置信息"
        ordering = ("-create_time",)
        # indexes = [
        #     models.Index(fields=['id','type','host','dbname'])
        # ]
        unique_together = ('id','type','host','dbname') # 必须加主键ID

    def __str__(self):
        return f"{self.name}/{self.host}/{self.port}/{self.dbname}"

class Redis(models.Model):
    name = models.CharField(max_length=128, unique=True,verbose_name="备注信息")
    host = models.CharField(max_length=64, verbose_name="服务器地址")
    username = models.CharField(max_length=64, verbose_name="登录用户")
    password = models.CharField(max_length=64, null=True,verbose_name="密码")
    db = models.SmallIntegerField(default=1, verbose_name="数据库")
    port = models.IntegerField(default=6379, verbose_name="端口")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    class Meta:
        db_table = table_prefix + "redis"
        verbose_name_plural = "REDIS配置信息"
        ordering = ("-create_time",)


class RabbitMQ(models.Model):
    name = models.CharField(max_length=128,unique=True,verbose_name="备注信息")
    host = models.CharField(max_length=64, verbose_name="服务器地址")
    username = models.CharField(max_length=64, verbose_name="登录用户")
    password = models.CharField(max_length=64, verbose_name="密码")
    vhost = models.CharField(max_length=64, null=True, verbose_name="vhost")
    exchange = models.CharField(max_length=128, null=True, verbose_name="交换机")
    producer = models.CharField(max_length=128, null=True, verbose_name="请求队列")
    consumer = models.CharField(max_length=128, null=True, verbose_name="消费队列")
    port = models.IntegerField(default=5672, verbose_name="端口")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    class Meta:
        db_table = table_prefix + "rabbitmq"
        verbose_name_plural = "MQ配置信息"
        ordering = ("-create_time",)


class FTP(models.Model):
    name = models.CharField(max_length=128,unique=True, verbose_name="备注信息")
    host = models.CharField(max_length=64, verbose_name="服务器地址")
    username = models.CharField(max_length=64, verbose_name="登录用户")
    password = models.CharField(max_length=64, verbose_name="密码")
    port = models.IntegerField(default=21, verbose_name="端口")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    class Meta:
        db_table = table_prefix + "ftp"
        verbose_name_plural = "FTP配置信息"
        ordering = ("-create_time",)
