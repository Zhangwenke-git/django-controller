import traceback
from django.core.exceptions import PermissionDenied
from rest_framework.views import exception_handler
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED, \
    HTTP_403_FORBIDDEN
from rest_framework.exceptions import (AuthenticationFailed, MethodNotAllowed, NotAuthenticated,
                                       PermissionDenied as RestPermissionDenied,
                                       ValidationError)
from sse.lib.core.response import APIResponse
from sse.lib.utils.logger import logger

logger = logger()


def exc_exceptions(exc, context):
    response = exception_handler(exc, context)
    # request = context["request"]._request

    try:
        code = exc.get_codes() if exc.get_codes() else 30001
    except Exception:
        code = 404
    error, status, msg = {"code": code,"message": str(exc)}, HTTP_400_BAD_REQUEST, "数据校验不通过,Invalid data"
    header = None
    if response is not None:
        if isinstance(response.data, dict):
            if response.data.get("detail"):
                error.update(message=response.data.get("detail"))
            else:
                field, tips = list(response.data.items())[0]
                try:
                    error.update(code=50002, message=tips["msg"].title())
                except TypeError:
                    error.update(code=50003, message=field + tips[0].title())

        if isinstance(response.data, list):
            error.update(code=50004, message=response.data[0].title())

        if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
            # 认证失败后，返回登录的地址，并重定向当前地址，并放入到消息头中返回
            request = context["request"]._request
            current_row_path = request.get_raw_uri()

            host = request.scheme + "://" + request.get_host()
            login_url = host + "/user/login/"
            redirect_url = login_url + "&redirect=" + current_row_path
            response.headers.setdefault("redirect", redirect_url)
            status = HTTP_401_UNAUTHORIZED

    else:
        error.update(status=30005, message="服务器内部错误")
        status = HTTP_500_INTERNAL_SERVER_ERROR

        # 调试模式
        logger.error(traceback.format_exc())
        traceback.format_exc()

        try:
            header = response.headers
        except AttributeError:
            msg="Uncaptured exception"
    return APIResponse(error=error, result=False, msg=msg, headers=header, status=status)
