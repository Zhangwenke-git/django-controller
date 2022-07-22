import json
import os,re
import redis
from django.forms import model_to_dict
from django.http import HttpResponse, StreamingHttpResponse
from pathlib import Path
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header
from user.auther import Authenticator
from django.shortcuts import render
from user.permissions import PermissionChecker
from rest_framework.parsers import JSONParser
from sse.lib.core.model_view_set import RewriteModelViewSet
from api.models import Project, Scenario, Templates, TestCase, TestSuit, ExecutionRecord,ExecutionRequestBackup,CrontabExecID
from api.model_serializer import ProjectSerializer, TestCaseSerializer, TestSuitSerializer, \
    TemplateSerializer, ScenarioSerializer, ExecutionRecordSerializer
from api.filter import ProjectFilter, TemplateFilter, TestCaseFilter, TestSuitFilter, \
    ExecutionRecordFilter, ScenarioFilter
from django.views.decorators.csrf import csrf_exempt
from sse.lib.core.case_parser import case_parser,module_parser,project_parser
from sse.lib.utils.logger import logger
from sse.celery_job.tasks import celery_exec_request
from sse.lib.utils.config_parser import ConfigParser
from sse.lib.utils.FtpUtils import FTPHelper
from sse.lib.core.period_task import *
from sse.lib.core.cron_task import *
from sse.lib.utils.parser_template import parameterized_fields
from sse.lib.utils.Requester import request_
from api.data_type_parser import parser_request_info
from django_celery_beat.models import PeriodicTask

ip, port, user, pwd = ConfigParser().read_ftp_info

logger = logger()
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ProjectViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser == 1:
            return Project.objects.all()
        return Project.objects.filter(owner=user.user_id)  # 仅管理员才可以查看所有的项目；仅自己才可以查看自己的项目

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # throttle_scope = "project_view"
    filter_class = ProjectFilter


class TestSuitViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = TestSuitSerializer
    queryset = TestSuit.objects.all()
    filter_class = TestSuitFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TestCaseViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = TestCaseSerializer
    queryset = TestCase.objects.all()
    filter_class = TestCaseFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TemplateViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = TemplateSerializer
    queryset = Templates.objects.all()
    filter_class = TemplateFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ScenarioViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()
    filter_class = ScenarioFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = ExecutionRecordSerializer
    queryset = ExecutionRecord.objects.all()
    filter_class = ExecutionRecordFilter

    def perform_create(self, serializer):
        serializer.save(person=self.request.user)




@csrf_exempt
def execute(request):
    token = get_authorization_header(request)
    user = jwt_decode_handler(token)

    data = json.loads(request.body.decode())

    try:
        if data["type"] == "case":
            body = [case_parser(data)]
            type = 2
        elif data["type"] == "module":
            type = 1
            body = module_parser(data)
        elif data["type"] == "project":
            type = 0
            body = project_parser(data)
        else:
            raise NotImplementedError("Type error,only including case,module and project.")
        setting=data['setting']
        code =data["id"]
        ExecutionRecord.objects.create(
            code=code,
            remark=setting.get('remark'),
            start=datetime.now(),
            type=type,
            task_type=setting["task_type"],
            stick_start_point=setting.get("start_point"),
            loop_interval=setting["interval"],
            person=user["user_id"]
        )
    except Exception as e:
        logger.error(f"Fail to parser data,due to error:{str(e)}")
        res = {"success": False, "message": "执行请求发送失败！"}
    else:
        message = {"exec_id": code, "body": body}
        logger.debug(f"Success to insert a record,exec_id:[{data['id']}]")
        task_type=setting['task_type']

        if task_type=="0":
            type_="普通任务"
            task_name = None
            celery_exec_request.delay(message)

        elif task_type=="1":
            type_="定时任务: "+setting["start_point"]
            task_name = cron_task_create(setting["start_point"],message)

        elif task_type=="2":
            type_="轮询任务: 周期-"+str(setting["interval"]*10) +"min"
            task_name = period_task_create(setting["interval"],message)

        if int(task_type) in [1,2]:
            CrontabExecID.objects.create(code=code,task=task_name,task_type=int(task_type))
            ExecutionRecord.objects.filter(code=code).update(cron_task_status=1)

        callback = {"id":code,"type":type_}
        res = {"success": True, "message": callback}



        # t = threading.Thread(target=exec_request, args=(message,))  # 将请求参数发给后端执行引擎，开启子线程，t.setDaemon(False)并不再等待返回结果
        # t.setDaemon(False)
        # t.start()

    return HttpResponse(json.dumps(res, ensure_ascii=False))


@csrf_exempt
def batch_execute(request):
    token = get_authorization_header(request)
    user = jwt_decode_handler(token)

    data = json.loads(request.body.decode())

    try:
        if data["type"] == "case":
            type = 2
            body = module_parser(data)
        elif data["type"] == "module":
            type = 1
            body = project_parser(data)
        else:
            raise NotImplementedError("Type error,only including case and module.")

        ExecutionRecord.objects.create(
            code=data["id"],
            remark=data.get('remark'),
            start=datetime.datetime.now(),
            type=type,
            person=user["user_id"]
        )
    except Exception:
        res = {"success": False, "message": "批量执行请求发送失败！"}
    else:
        message = {"exec_id": data['id'], "body": body}
        logger.debug(f"Success to insert a batched record,exec_id:[{data['id']}]")
        res = {"success": True, "message": f"批量执行请求发送成功，执行编码【{data['id']}】，请访问测试报告面板查看结果！"}

        celery_exec_request.delay(message)

    return HttpResponse(json.dumps(res, ensure_ascii=False))


@csrf_exempt
def re_execute(request):
    token = get_authorization_header(request)
    user = jwt_decode_handler(token)
    data = json.loads(request.body.decode())
    exec_id = data['exec_id']
    backup=ExecutionRequestBackup.objects.filter(code=exec_id).first()
    if backup:
        ExecutionRecord.objects.filter(code=exec_id).update(statue=0,person=user["user_id"])
        res = {"success": True, "message": f"重复执行请求发送成功，执行编码【{exec_id}】，请访问测试报告面板查看结果！"}
        celery_exec_request.delay(message=backup.body,re_flag=True)
    else:
        res = {"success": False, "message": f"重复执行请求发送失败，执行编码【{exec_id}】执行记录不存在"}

    return HttpResponse(json.dumps(res, ensure_ascii=False))

@csrf_exempt
def report_view(request):
    data = json.loads(request.body.decode())
    exec_id = data['exec_id']

    ant_report_dir = os.path.join(BASE_DIR, r'templates\ant')
    for root, dirs, files in os.walk(ant_report_dir):
        if '%s.html' % exec_id in files:
            logger.debug(
                f"Report [{exec_id}.html] has already existed in temporary folder,and there is no need to download from FTP server.")
        else:
            logger.debug(f"Start to download report from FTP server.")
            report = ExecutionRecord.objects.filter(code=exec_id, statue=0).first()
            if report:
                remote_path = report.path
                logger.debug(f"Report on FTP server path is:{remote_path},and prepare to download correlated report.")
                ftp = FTPHelper(ip=ip, password=pwd, port=port, username=user)
                ftp.download_file(ant_report_dir, remote_path)
                ftp.close()
            else:
                logger.error(f"Fail to find record about EXEC_CODE:{exec_id},whose status is success.")

    return render(request, 'ant/%s.html' % exec_id)

@csrf_exempt
def parameter_fields(request):
    data = json.loads(request.body.decode())
    case_uuid = data["case"]
    case = TestCase.objects.all().filter(uid=case_uuid).first()
    case_template = case.template.data
    fields,func_dict_list = parameterized_fields(case_template)
    default = case.template.default
    res = {"success": False, "fields":fields,"func_dict_list": func_dict_list,"default":default}
    return HttpResponse(json.dumps(res, ensure_ascii=False))

@csrf_exempt
def process_parameterized_fields(request):
    data = json.loads(request.body.decode())
    fields,func_dict_list = parameterized_fields(data)
    res = {"success": True, "fields":fields,"func_dict_list": func_dict_list}
    return HttpResponse(json.dumps(res, ensure_ascii=False))


@csrf_exempt
def process_request(request):
    data = json.loads(request.body.decode())
    request_info = parser_request_info(data)
    res = request_(method=request_info.get("method"), url=request_info["url"], headers=request_info.get("header"), data=request_info.get("data"))
    message = json.dumps(res,ensure_ascii=False,indent=4)
    res = {"success": True, "message": message}
    return HttpResponse(json.dumps(res, ensure_ascii=False))



@csrf_exempt
def make_request(request,pk):
    import requests
    obj =  Templates.objects.get(uid=pk)
    if obj:
        obj = model_to_dict(obj)
        print(obj)
        request_info = parser_request_info(obj)
        try:
            res = request_(method=request_info.get("method"), url=request_info["url"], headers=request_info.get("header"),
                           data=request_info.get("data"))
            message = json.dumps(res, ensure_ascii=False, indent=4)
        except TimeoutError:
            message='Time out'
        except requests.exceptions.ConnectTimeout:
            message = 'ConnectTimeout'
        res = {"success": True, "message": message}
        return HttpResponse(json.dumps(res, ensure_ascii=False))

@csrf_exempt
def oneKeyExpression(request):
    data = json.loads(request.body.decode())
    obj =  Templates.objects.get(uid=data["interfaceName"])
    res = {"success": False, "expression": ""}
    if obj:
        expression_ = data["expression"]
        expressions = ["%s:%s" % (item["field"],item["express"]) for item in expression_]
        expression = ",".join(expressions)
        expression = "@{%s}|{%s}" % (obj.name,expression)
        res = {"success": True, "expression": expression}
    return HttpResponse(json.dumps(res, ensure_ascii=False))

@csrf_exempt
def report_download(request, pk=None):
    """
    文件下载
    :return: 文件流对象
    """
    # 迭代读取文件
    def file_iterator(file_path, chunk_size=512):
        with open(file_path, 'rb') as f:
            while True:
                content = f.read(chunk_size)
                if content:
                    yield content
                else:
                    break

    file_dir = os.path.join(BASE_DIR, 'templates/ant')
    file_name = f'{pk}.html'

    download_file = os.path.join(file_dir, file_name)
    if not os.path.isfile(download_file):
        logger.debug(f"Start to download report from FTP server.")
        report = ExecutionRecord.objects.filter(code=pk, statue=0).first()
        if report:
            remote_path = report.path
            logger.debug(f"Report on FTP server path is:{remote_path},and prepare to download correlated report.")
            ftp = FTPHelper(ip=ip, password=pwd, port=port, username=user)
            ftp.download_file(file_dir, remote_path)
            ftp.close()
        else:
            logger.error(f"Fail to find record about EXEC_CODE:{pk},whose status is success.")

    response = StreamingHttpResponse(file_iterator(download_file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response

@csrf_exempt
def stop_task(request,pk):
    res = {"success":True,"message":"停止任务成功"}
    crontab_obj = CrontabExecID.objects.get(code=pk,task_type__in=[1,2])
    if crontab_obj:
        if crontab_obj.task_type == 1:
            cron_task_stop(crontab_obj.task)
        else:
            period_task_stop(crontab_obj.task)
        ExecutionRecord.objects.filter(code=pk).update(cron_task_status=3)
    return HttpResponse(json.dumps(res,ensure_ascii=False))

@csrf_exempt
def delete_task(request,pk):
    res = {"success":True,"message":"删除任务成功"}
    crontab_obj = CrontabExecID.objects.get(code=pk,task_type__in=[1,2])
    if crontab_obj:
        if crontab_obj.task_type == 1:
            cron_task_delete(crontab_obj.task)
        else:
            period_task_delete(crontab_obj.task)
        ExecutionRecord.objects.filter(code=pk).update(cron_task_status=4)
    return HttpResponse(json.dumps(res,ensure_ascii=False))


@csrf_exempt
def restore_task(request,pk):
    res = {"success": True, "message": "恢复任务成功"}
    crontab_obj = CrontabExecID.objects.get(code=pk, task_type__in=[1, 2])
    if crontab_obj:
        if crontab_obj.task_type == 1:
            cron_task_restore(crontab_obj.task)
        else:
            period_task_restore(crontab_obj.task)
        ExecutionRecord.objects.filter(code=pk).update(cron_task_status=1)
    return HttpResponse(json.dumps(res, ensure_ascii=False))
