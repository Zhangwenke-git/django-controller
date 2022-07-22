# -*-coding=utf8-*-
import uuid
from django.db import models
from django.utils.safestring import mark_safe
from user.models import UserProfile
from django.conf import settings
table_prefix = settings.TABLE_PREFIX



class UUIDTools(object):

    @staticmethod
    def uuid4_hex():
        return str(uuid.uuid4()).replace("-","")


class BaseModel(models.Model):
    statue_choice = (
        (0, "作废"),
        (1, "有效"),
    )
    uid = models.CharField(primary_key=True, max_length=64,auto_created=True, default=UUIDTools.uuid4_hex, editable=False,verbose_name="UID")
    statue = models.SmallIntegerField(choices=statue_choice, default=1, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    owner = models.ForeignKey(UserProfile,null=True, verbose_name='所属用户', on_delete=models.CASCADE)

    class Meta:
        abstract=True



class Project(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名称')
    description = models.CharField(max_length=320, blank=True, null=True, verbose_name='项目描述')
    start = models.DateField(max_length=64, blank=True, null=True, verbose_name='项目开始')
    end = models.DateField(max_length=64, blank=True, null=True, verbose_name='项目结束')
    process = models.PositiveSmallIntegerField(default=0, verbose_name="项目进度")
    last_execute = models.PositiveSmallIntegerField(default=0, verbose_name="最近一次执行成功率")


    class Meta:
        db_table = table_prefix + "project"
        verbose_name_plural = 'API项目管理'
        ordering = ('-update_time',)

    def __str__(self):
        return self.name


class TestSuit(BaseModel):
    module = models.CharField(max_length=64, unique=True, verbose_name='Py文件名称')
    class_title = models.CharField(max_length=32, blank=True, null=True, verbose_name='测试类名称')
    project = models.ManyToManyField(Project, verbose_name='所属项目')

    class Meta:
        db_table = table_prefix + "suit"
        verbose_name_plural = '用例集'
        ordering = ('-update_time',)

    def __str__(self):
        return self.module

    @property
    def projects(self):
        project_list = Project.objects.all()
        projects =[project.name for project in project_list]
        return projects


def default_header():
    return {"Content-Type": "application/json"}


class Templates(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name='模板名称')
    url = models.URLField(max_length=128, verbose_name='URL地址')
    method_choice = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.SmallIntegerField(choices=method_choice, default=1, verbose_name="请求方式")
    header = models.JSONField(null=True, default=default_header, verbose_name='headers')
    data = models.JSONField(verbose_name='请求模板', null=True)
    default = models.JSONField(verbose_name='参数默认值',null=True)
    expect = models.JSONField(verbose_name='结果解析表达式',null=True)
    process_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='进程名称')
    linux_order_str = models.CharField(max_length=100, blank=True, null=True, verbose_name='linux命令')
    sql = models.CharField(max_length=1024, blank=True, null=True, verbose_name='校验SQL')
    dbinfo = models.CharField(max_length=128, blank=True, null=True, verbose_name='数据库信息')


    class Meta:
        db_table = table_prefix + "templates"
        verbose_name_plural = '请求接口模板'
        ordering = ('-update_time',)
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class TestCase(BaseModel):
    case = models.CharField(max_length=64, unique=True, verbose_name='测试用例')
    case_title = models.CharField(max_length=100, verbose_name='测试用例名称')
    case_description = models.CharField(max_length=320, blank=True, null=True, verbose_name='测试用例描述')
    template = models.ForeignKey(Templates, verbose_name='模板', on_delete=models.CASCADE)
    testsuit = models.ForeignKey(TestSuit, verbose_name='用例集合', on_delete=models.CASCADE,related_name='suit_case')
    priority_choice = (
        (0, "高"),
        (1, "中"),
        (2, "低"),
    )
    priority = models.SmallIntegerField(choices=priority_choice, default=0, verbose_name="优先级")
    class Meta:
        db_table = table_prefix + "case"
        verbose_name_plural = '用例函数'
        ordering = ('-update_time',)
        indexes = [
            models.Index(fields=['case'])
        ]
    @property
    def templates_name(self):
        return self.templates.name

    @property
    def testsuit_name(self):
        return self.testsuit.module

    def __str__(self):
        return "%s-%s" % (self.case_title, self.case)


class Scenario(BaseModel):
    scenario = models.CharField(max_length=64, unique=True, verbose_name='场景名称')
    parameter = models.JSONField(verbose_name='请求参数',null=True)
    validator = models.JSONField(verbose_name='验证字段',null=True)
    cases = models.ForeignKey(TestCase, verbose_name='测试函数（用例）',related_name='case_scenario', on_delete=models.CASCADE)

    class Meta:
        db_table = table_prefix + "scenario"
        verbose_name_plural = '用例场景'
        ordering = ('-update_time',)
        indexes = [
            models.Index(fields=['scenario'])
        ]
    @property
    def testcase_name(self):
        return self.testcase.case

    def __str__(self):
        return self.scenario  # 不添加这个的话，多对多关系中会提示：XXX.onject1,XXX.onject2,


class ExecutionRecord(models.Model):
    statue_choice = (
        (0, "执行完毕"),
        (1, "执行中"),
        (2, "执行超时"),
        (3, "执行异常"),
        (4, "未启动"),
    )
    type_choice = (
        (0, "测试项目"),
        (1, "测试套件"),
        (2, "测试用例"),
        (3,"未知")
    )
    task_type_choice = (
        (0,"普通任务"),
        (1,"定时任务"),
        (2,"轮询任务"),
    )

    cron_task_status_choice = (
        (1,"运行中"),
        (2,"已结束"),
        (3,"暂停"),
        (4,"已删除"),
        (5,"过期"),
    )

    code = models.CharField(max_length=64,primary_key=True, verbose_name='执行编码')
    remark = models.CharField(max_length=128, verbose_name='执行备注',null=True,blank=True)
    statue = models.SmallIntegerField(choices=statue_choice,default=4, verbose_name="状态")
    type = models.SmallIntegerField(choices=type_choice, default=3,verbose_name="类型")
    cron_task_status = models.SmallIntegerField(choices=cron_task_status_choice,null=True, default=None,verbose_name="类型")
    task_type = models.SmallIntegerField(choices=task_type_choice, default=0,verbose_name="任务类型")
    stick_start_point = models.DateTimeField(null=True,verbose_name="定时任务时间点")
    loop_interval = models.SmallIntegerField(null=True, verbose_name="轮询任务时间间隔")
    start = models.CharField(max_length=32, verbose_name='开始执行时间')
    path = models.CharField(max_length=128, verbose_name='FTP报告路径',null=True,blank=True)
    duration = models.CharField(max_length=32, verbose_name='耗时',null=True,blank=True)
    person = models.CharField(max_length=32, verbose_name='执行人员')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_date = models.DateField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        db_table = table_prefix + "record"
        verbose_name_plural = '执行记录'
        ordering = ('-update_time',)
        indexes = [
            models.Index(fields=['code'])
        ]

    def __str__(self):
        return "%s-%s" % (self.code,self.remark)



class ExecutionRequestBackup(models.Model):
    code =  models.CharField(max_length=64,primary_key=True, verbose_name='执行编码')
    body=models.JSONField(verbose_name='请求体')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        db_table = table_prefix + "request_backup"
        verbose_name_plural = '执行请求备份'
        ordering = ('-update_time',)
        indexes = [
            models.Index(fields=['code'])
        ]


class CrontabExecID(models.Model):
    task_type_choice = (
        (0,"普通任务"),
        (1,"定时任务"),
        (2,"轮询任务"),
    )
    code = models.CharField(max_length=64,null=True, verbose_name='执行编码')
    task = models.CharField(max_length=64, null=True, verbose_name='定时任务名称')
    task_type = models.SmallIntegerField(choices=task_type_choice, null=True, verbose_name="任务类型")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    class Meta:
        db_table = table_prefix + "crontab_exec"
        verbose_name_plural = '定时任务和执行编码对照表'
        ordering = ('-create_time',)
        indexes = [
            models.Index(fields=['code'])
        ]
    def __str__(self):
        return "%s-%s" % (self.code, self.task)
