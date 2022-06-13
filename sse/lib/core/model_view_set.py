import json

from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from .response import APIResponse
from sse.lib.utils.logger import logger
logger = logger()
class RewriteModelViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return APIResponse(msg="创建成功",result=True,data=response.data,status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return APIResponse(msg="查看详情",result=True,data=response.data,status=HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return APIResponse(msg="更新成功",result=True,data=response.data,status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return APIResponse(msg="删除成功",result=True,data=None,status=HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return APIResponse(msg="success",result=True,data=response.data,status=HTTP_200_OK)