import re
from rest_framework import serializers
from user.models import UserProfile,Role,Menu
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.conf import settings
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler




# 想返回该字段，但提交post的时候不写入，则使用read_only即可
class UserProfileSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=16, min_length=8, required=True, write_only=True)

    class Meta:
        model = UserProfile
        fields = ["user_id", "name", "password", "mobile", "email", "re_password","role"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def checke_(self,string,pattern):
        match_re = re.compile(pattern)
        res = re.search(match_re, string)
        return True if res else False

    # 局部钩子
    def validate_mobile(self, data):
        if not len(data) == 11:
            raise ValidationError({'msg': '手机号必须等于11位'})
        if not self.checke_(data,r"^1[3-9][0-9]{9}$"):
            raise ValidationError({'msg': '无效手机号'})
        return data

    def validate_user_id(self, data):
        if len(data) > 16:
            raise ValidationError({'msg': '用户ID不可长于16位'})
        if len(data) < 4:
            raise ValidationError({'msg': '用户ID不可少于4位'})
        if not self.checke_(data,"[a-zA-z]\\w{1,15}$"):
            raise ValidationError({'msg': '无效用户名'})
        return data


    def validate_password(self, data):
        if len(data) < 8:
            raise ValidationError({'msg': '密码不能少于8位有效字符'})
        if len(data) > 16:
            raise ValidationError({'msg': '密码不能长于18位有效字符'})
        if not self.checke_(data, pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"):
            raise ValidationError({'msg': '密码需包含字母大小写、数字和特殊字符'})
        return data

    # 全局钩子,优先走该方法
    def validate(self, attrs):
        if not attrs.get("password") == attrs.get("re_password"):
            raise ValidationError("两次输入的密码不一致")
        return attrs

    def create(self, validated_data):
        validated_data.pop("re_password")
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if not validated_data.get("user_id") == instance.user_id:
            raise ValidationError("user_id不可以被修改")
        else:
            validated_data.pop("re_password")
            validated_data.pop("password")
            instance.name = validated_data.get('name', instance.name)
            instance.password = make_password(validated_data.get('password', instance.password))
            instance.mobile = validated_data.get('mobile', instance.mobile)
            instance.email = validated_data.get('email', instance.email)
            # instance.role = validated_data.get('role',instance.role)
            instance.save()
            return instance


class LoginSerializer(serializers.ModelSerializer):
    # 覆盖，避免login校验username有数据库唯一字段约束的限制
    user_id = serializers.CharField()

    class Meta:
        model = UserProfile

        fields = ('user_id', 'email', 'mobile', 'password', 'upload')
        extra_kwargs = {
            'password': {'write_only': True},
            'upload': {'read_only': True},
            'email': {'read_only': True},
            'mobile': {'read_only': True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    def _get_user(self, attrs):
        user_id = attrs.get('user_id')
        if re.match(r'^1[3-9][0-9]{9}$', user_id):
            user = UserProfile.objects.filter(mobile=user_id).first()
        elif re.match(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', user_id):
            user = UserProfile.objects.filter(email=user_id).first()
        else:
            user = UserProfile.objects.filter(user_id=user_id).first()
        if not user:
            raise ValidationError({'user_id': '请求报文校验不通过，账号信息填写错误'})
        password = attrs.get('password')
        if not user.check_password(password):
            raise ValidationError({'password': '请求报文校验不通过，密码填写错误'})
        return user

    def _get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token






class MenuSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    class Meta:
        model = Menu
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    class Meta:
        model = Role
        fields = "__all__"

class UserProfileDetailsSerializer(serializers.ModelSerializer):
    statue_display = serializers.CharField(source='get_statue_display', read_only=True)
    sex_display = serializers.CharField(source='get_sex_display', read_only=True)
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        queryset = obj.role.all()
        roles = '|'.join([row.name for row in queryset])
        return roles
    class Meta:
        model = UserProfile
        exclude = ["password",]

