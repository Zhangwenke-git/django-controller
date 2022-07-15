#filters.py
from django_filters import rest_framework as filters
from user.models import UserProfile


class UserProfileFilter(filters.FilterSet):
    user_id = filters.CharFilter(field_name="user_id", lookup_expr='icontains')
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    statue = filters.NumberFilter(field_name="statue", lookup_expr='icontains')
    class Meta:
        model = UserProfile  # 模型名
        fields = ["user_id","name","statue"]
