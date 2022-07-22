from rest_framework.parsers import JSONParser

from user.auther import Authenticator
from user.permissions import PermissionChecker
from .model_serializer import *

class DatabaseViewSet(BulkModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]
    pagination_class = None

    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    # def allow_bulk_destroy(self, qs, filtered):
    #     return True

class RedisViewSet(BulkModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]
    pagination_class = None

    queryset = Redis.objects.all()
    serializer_class = RedisSerializer

class RabbitMQViewSet(BulkModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]
    pagination_class = None

    queryset = RabbitMQ.objects.all()
    serializer_class = RabbitMQSerializer

class FTPViewSet(BulkModelViewSet):
    parser_classes = [JSONParser, ]
    authentication_classes = [Authenticator, ]
    permission_classes = [PermissionChecker, ]
    pagination_class = None

    queryset = FTP.objects.all()
    serializer_class = FTPMQSerializer