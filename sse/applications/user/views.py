import datetime

from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet, ViewSet

from sse.lib.core.model_view_set import RewriteModelViewSet
from sse.lib.core.response import APIResponse
from sse.lib.utils.logger import logger
from user.auther import Authenticator
from user.permissions import PermissionChecker
from .filter import UserProfileFilter

logger = logger()

from user.model_serializer import *


class LoginViewSet(ViewSet):
    # 局部禁用认证、权限组件
    authentication_classes = ()
    permission_classes = ()

    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            token = serializer.context.get('token')

            # 拿到登录用户，直接走序列化过程，将要返回给前台的数据直接序列化好给前台
            user = serializer.context.get('user')
            result = LoginSerializer(user, context={'request': request}).data
            result['token'] = token
            return APIResponse(code=1002, msg="登录成功", data=result,
                               login_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        return APIResponse(code=1003, msg="登录失败", status=HTTP_400_BAD_REQUEST, result=False,
                           error=list(serializer.errors.values())[0][0])


class RegisterUserProfileView(GenericViewSet, CreateModelMixin):  # 一般genericView都会配置Mixin扩展类
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UpdateUserProfileView(GenericViewSet, UpdateModelMixin):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserProfilesListView(ListAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = UserProfileDetailsSerializer
    queryset = UserProfile.objects.all()
    filter_class = UserProfileFilter
    throttle_scope = "user_view"
    authentication_classes = [Authenticator, ]


class UserProfilesDetailsView(DestroyAPIView, RetrieveAPIView):
    authentication_classes = [Authenticator, ]
    serializer_class = UserProfileDetailsSerializer
    queryset = UserProfile.objects.all()


class RoleViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]

    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class MenuViewSet(RewriteModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


import json
from user.models import UserProfile
from functools import reduce
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def merge_list(x: list, y: list):
    return x.extend(y)


@csrf_exempt
def user_menus(request):
    data = json.loads(request.body.decode())
    user_id = data["user_id"]
    user = UserProfile.objects.get(user_id=user_id)
    menus = []
    if user:
        roles = user.role.all()
        for role in roles:
            menu_objs = role.menu.all()
            pids = []
            for menu_obj in menu_objs:
                if menu_obj.pid > 0:
                    pids.append(menu_obj.pid)
                else:
                    ...
            pids = list(set(pids))
            pids_list = [model_to_dict(obj) for obj in Menu.objects.filter(rid__in=pids)]
            menus_list = [model_to_dict(obj) for obj in menu_objs]
            menus_list.extend(pids_list)
            menus.append(menus_list)
        if len(menus) > 0:
            menus = list(reduce(merge_list, menus))
        print(menus)
    return HttpResponse(json.dumps({"message": menus}, ensure_ascii=False))
