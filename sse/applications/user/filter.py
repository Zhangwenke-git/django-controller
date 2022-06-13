#filters.py
from django_filters import rest_framework as filters
from user.models import UserProfile


class UserProfileFilter(filters.FilterSet):
    user_id = filters.CharFilter(field_name="user_id", lookup_expr='icontains')
    is_active = filters.NumberFilter(field_name="is_active", lookup_expr='icontains')
    class Meta:
        model = UserProfile  # 模型名
        fields = ["user_id","is_active"]
