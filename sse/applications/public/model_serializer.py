from rest_framework.serializers import ModelSerializer
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    BulkModelViewSet
)
from .models import *


class DatabaseSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = Database
        fields = "__all__"
        list_serializer_class = BulkListSerializer

class RedisSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = Redis
        fields = "__all__"
        list_serializer_class = BulkListSerializer

class RabbitMQSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = RabbitMQ
        fields = "__all__"
        list_serializer_class = BulkListSerializer

class FTPMQSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = FTP
        fields = "__all__"
        list_serializer_class = BulkListSerializer

