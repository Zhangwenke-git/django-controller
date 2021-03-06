import datetime
import json
import os,re
from django.http import HttpResponse
from pathlib import Path
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header
from user.auther import Authenticator
from django.shortcuts import render
from user.permissions import PermissionChecker
from rest_framework.parsers import JSONParser
from sse.lib.core.model_view_set import RewriteModelViewSet
from api.models import Project, Scenario, Templates, TestCase, TestSuit, ExecutionRecord
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

        ExecutionRecord.objects.create(
            code=data["id"],
            remark=data.get('remark'),
            start=datetime.datetime.now(),
            type=type,
            person=user["user_id"]
        )
    except Exception as e:
        logger.error(f"Fail to parser data,due to error:{str(e)}")
        res = {"success": False, "message": "执行请求发送失败！"}
    else:
        message = {"exec_id": data['id'], "body": body}
        logger.debug(f"Success to insert a record,exec_id:[{data['id']}]")
        res = {"success": True, "message": f"执行请求发送成功，执行编码【{data['id']}】，请访问测试报告面板查看结果！"}

        celery_exec_request.delay(message)

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

    def remove_character(string: str):
        character = ['$', '{', '}']
        for char_ in character:
            string = string.replace(char_, '')
        return string

    filed_pattern = r'\{{(.+?)\}}'
    comment = re.compile(filed_pattern, re.DOTALL)
    field_list = comment.findall(json.dumps(case_template))
    fields = list(map(remove_character, field_list))
    fields = list(set(fields))

    func_pattern = r'\$\{.+?>'
    comment = re.compile(func_pattern, re.DOTALL)
    func_list = comment.findall(json.dumps(case_template))
    func = list(map(remove_character, func_list))
    fields = list(set(fields))
    func_dict_list = []
    for fun in func:
        func_dict = {}
        fun_list = fun.split("|")
        try:
            func_dict[fun_list[0]] = fun_list[1]
        except IndexError:
            raise NameError(f"The separative sign '|' in function string: [{fun_list[0]}] not found!")
        func_dict = {k: list(v.replace('<', '').replace('>', '').split(',')) for k, v in
                     func_dict.items()}  # 处理参数的中特殊字符，并转换成tuple格式
        func_dict_list.append(func_dict)

    for temp in func_dict_list:
        for k, v in temp.items():
            if v[0] == "":
                temp.update({k: None})
            else:
                pass

    res = {"success": False, "fields":fields,"func_dict_list": func_dict_list}
    print(res)
    return HttpResponse(json.dumps(res, ensure_ascii=False))
