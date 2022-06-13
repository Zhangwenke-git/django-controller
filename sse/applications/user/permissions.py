from rest_framework.permissions import BasePermission,SAFE_METHODS

class PermissionChecker(BasePermission):
    message = '此操作未授权。Operation is not granted'

    def has_permission(self, request, view):
        user_obj = request.user
        return bool(user_obj.is_active == 1)

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS:
            # 只读权限校验
            flag=True
        else:
            # 仅管理员和自己，才可以删除和修改记录
            user_obj = request.user
            flag =  bool(user_obj.is_staff or user_obj.user_id == request.user)
        return flag
