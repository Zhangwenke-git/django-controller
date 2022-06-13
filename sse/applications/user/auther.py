import jwt,time
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from sse.lib.utils.logger import logger
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header
from sse.lib.utils.SM4 import SM4
from sse.lib.utils.config_parser import ConfigParser
from sse.settings.dev import HEADER_CHECKER

CONSTANT = ConfigParser()
sm4 = SM4()

logger = logger()

'''  
    #重中之重
        token = get_authorization_header(request)
        payload = jwt_decode_handler(token)
'''


class Authenticator(JSONWebTokenAuthentication):
    def authenticate(self, request):
        headers = request._request.headers
        token = get_authorization_header(request)
        if not token:
            raise AuthenticationFailed('消息头中Authorization为必填写字段')

        if HEADER_CHECKER:
            if not headers.get("uri"):
                raise AuthenticationFailed(detail="消息头中uri为必填写字段",code=4003)

            if not headers.get("nonce"):
                raise AuthenticationFailed("消息头中nonce为必填写字段")

            if not headers.get("timestamp"):
                raise AuthenticationFailed("消息头中timestamp为必填写字段")
            else:
                current_timestamp = time.time()
                upper = int(str(int(current_timestamp)) + "000") + CONSTANT.read_expire_internal
                lower = int(str(int(current_timestamp)) + "000") - CONSTANT.read_expire_internal
                if int(headers.get("timestamp")) <= upper and int(headers.get("timestamp")) >=lower:
                    ...
                else:
                    raise AuthenticationFailed(detail="消息头中timestamp已超时",code=4002)

            if not headers.get("sign"):
                raise AuthenticationFailed("消息头中sign为必填写字段")
            else:
                sign = headers["sign"]
                try:
                    row_sign = sm4.decrypt(CONSTANT.read_encrypt_key, sign)
                except Exception:
                    raise AuthenticationFailed("签名错误，无法解密")

                nonce = headers["Nonce"]
                timestamp = headers["Timestamp"]
                uri = headers["Uri"]
                params = request.path + ";" + nonce + ";" + timestamp + ";"

                row_sign_ = params + headers["Authorization"].split(".")[-1]
                sign_ = sm4.encrypt(CONSTANT.read_encrypt_key, row_sign_)

                if sign_ == sign:
                    logger.debug(f"timestamp={timestamp}, nonce={nonce},request_path={request.path},uri={uri}")
                    logger.info("Signature is correct and authentication is passed")

                else:
                    logger.debug(f"received sign={sign},and row_sign={row_sign},but correct sign={sign_}")
                    raise AuthenticationFailed('签名错误')

                """
                    # 加密规则
                        row-egw-param:requestPath;nonce;timestamp;
                        Authorization:token
                        row_sign = egw-param + Authorization.split(".")[-1]
                """

        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise AuthenticationFailed(detail='签名过期',code=40001)
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('非法用户')

        user_obj = self.authenticate_credentials(payload)

        return user_obj, token

    def authenticate_header(self, request):
        ...

