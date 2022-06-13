import json, uuid

import sentry_sdk
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from sse.lib.utils.logger import logger

logger = logger()


def _uuid():
    return str(uuid.uuid4())


def _get_request_headers(request):
    headers = {}
    for k, v in request.META.items():
        if k.startswith('HTTP_'):
            headers[k[5:].lower()] = v
    return headers


def _get_response_headers(response):
    headers = {}
    headers_tuple = response.headers.items()
    for k,v in headers_tuple:
        headers[k] = v
    return headers


NOT_SUPPORT_PATH = '/admin'  # 排除 admin 站点，admin 站点不会进入CollectionMiddleware的process_response方法，会导致报错


class CollectionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path.startswith(NOT_SUPPORT_PATH):
            pass
        else:
            if request.body:
                request.META['REQUEST_BODY'] = json.loads(
                    str(request.body, encoding='utf-8').replace(' ', '').replace('\n', '').replace('\t', ''),
                    strict=False)
            else:
                request.META['REQUEST_BODY'] = None

            if 'HTTP_X_FORWARDED_FOR' in request.META:
                remote_address = request.META['HTTP_X_FORWARDED_FOR']
            else:
                remote_address = request.META['REMOTE_ADDR']
            request.META['IP'] = remote_address
            request.META['LOG_UUID'] = _uuid()

    def process_response(self, request, response):
        if request.path.startswith(NOT_SUPPORT_PATH):
            pass
        else:
            if not isinstance(request.user, AnonymousUser):
                uid = request.user.user_id
            else:
                uid = None
            request.META['USER_UID'] = uid

            if response['content-type'] == 'application/json':
                if getattr(response, 'streaming', False):
                    response_body = '<<<Streaming>>>'
                else:
                    response_body = json.loads(str(response.content, encoding='utf-8'))
            else:
                response_body = '<<<Not JSON>>>'
            request.META['RESP_BODY'] = response_body

            try:
                request.META['VIEW'] = request.resolver_match.view_name
            except AttributeError:
                request.META['VIEW'] = None

            request.META['STATUS_CODE'] = response.status_code

        return response


class LoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if request.path.startswith(NOT_SUPPORT_PATH):
            pass
        else:
            logger.debug('Start LoggerMiddleware procedure and prepare to record log data')
            request_data = {
                "method": request.method,
                'path': request.get_full_path(),
                'view': request.META['VIEW'],
                'body': request.META['REQUEST_BODY'],
                'headers': _get_request_headers(request),
                'user_id': request.META['USER_UID'],
                "ip": request.META['IP'],
                'trace_id': request.META['LOG_UUID']
            }

            response_data = {
                'status': request.META['STATUS_CODE'],
                'body': request.META['RESP_BODY'],
                'headers': _get_response_headers(response),
                'trace_id': request.META['LOG_UUID']
            }

            logger.debug(f"Receive request: {json.dumps(request_data, ensure_ascii=False)}")
            logger.info(f"Receive request from IP: {request_data['ip']} by url: {request_data['path']} with method: {request_data['method']}")

            logger.debug(f"Return response: {json.dumps(response_data, ensure_ascii=False)}")

        return response


class SentryMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if request.path.startswith(NOT_SUPPORT_PATH):
            pass
        else:
            logger.debug('Start SentryMiddleware procedure and prepare to upload to Sentry')
            sentry_sdk.add_breadcrumb(
                category='path',
                message=request.path,
                level='debug',
            )

            sentry_sdk.add_breadcrumb(
                category='body',
                message=request.META["REQUEST_BODY"],
                level='debug',
            )

            sentry_sdk.add_breadcrumb(
                category='request_headers',
                message=_get_request_headers(request),
                level='debug',
            )

            sentry_sdk.add_breadcrumb(
                category='response_headers',
                message=_get_response_headers(response),
                level='debug',
            )

            sentry_sdk.add_breadcrumb(
                category='view',
                message=request.META['VIEW'],
                level='debug',
            )
            sentry_sdk.set_user({"id": request.META['USER_UID']})
            sentry_sdk.set_tag("trace_id", request.META["LOG_UUID"])
            sentry_sdk.capture_message(request.META["LOG_UUID"])

        return response
