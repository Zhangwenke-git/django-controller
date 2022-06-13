import datetime
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.parsers import JSONParser
from user.auther import Authenticator
from user.permissions import PermissionChecker
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView,UpdateAPIView
from sse.lib.core.response import APIResponse
from sse.lib.utils.logger import logger
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
        return APIResponse(code=1003, msg="登录失败", status=HTTP_400_BAD_REQUEST,result=False, error=list(serializer.errors.values())[0][0])


class RegisterUserProfileView(GenericViewSet, CreateModelMixin): #一般genericView都会配置Mixin扩展类
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator,]

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()



class UpdateUserProfileView(GenericViewSet, UpdateModelMixin):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator,]
    permission_classes = [PermissionChecker,]

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserProfilesListView(ListAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = UserProfileDetailsSerializer
    queryset = UserProfile.objects.all()
    filter_class = UserProfileFilter
    throttle_scope = "user_view"
    authentication_classes = [Authenticator,]


class UserProfilesDetailsView(DestroyAPIView, RetrieveAPIView):
    authentication_classes = [Authenticator,]
    serializer_class = UserProfileDetailsSerializer
    queryset = UserProfile.objects.all()



