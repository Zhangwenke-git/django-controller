import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
table_prefix = settings.TABLE_PREFIX



class UUIDTools(object):

    @staticmethod
    def uuid4_hex():
        return str(uuid.uuid4()).replace("-","")


class BaseModel(models.Model):
    statue_choice = (
        (0, "作废"),
        (1, "有效"),
    )
    _id = models.CharField(max_length=64,auto_created=True, unique=True,default=UUIDTools.uuid4_hex, editable=False,verbose_name="UID")
    statue = models.SmallIntegerField(choices=statue_choice, default=1, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        abstract=True


# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.safestring import mark_safe


class UserProfileManager(BaseUserManager):
    def create_user(self, user_id, password, email, name,mobile,role):
        if not user_id:
            raise ValueError('User must have an account id!')

        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            name=name,
            mobile=mobile,
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        user.role.add(*role)
        return user

    def create_superuser(self, user_id, password, email, name,mobile,role="superuser"):
        user = self.create_user(
            user_id=user_id,
            password=password,
            email=email,
            name=name,
            mobile=mobile,role=role
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = 1
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin,BaseModel):
    email = models.EmailField(verbose_name='邮箱',unique=True,max_length=255,)
    password = models.CharField(_('password'), max_length=128)

    is_choice = (
        (0, "否"),
        (1, "是"),
    )
    is_superuser = models.SmallIntegerField(choices=is_choice, default=0, verbose_name="超级用户")
    user_id = models.CharField(max_length=32, primary_key=True, null=False, blank=False, verbose_name='用户ID')
    USERNAME_FIELD = 'user_id'  # 作为唯一的登录标识

    mobile = models.CharField(max_length=11, unique=True,verbose_name='手机号码')
    name = models.CharField(max_length=32, verbose_name='用户名')

    sex_choice = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )
    sex = models.SmallIntegerField(choices=sex_choice, default=2, verbose_name="性别")
    role = models.ManyToManyField('Role',verbose_name='角色')
    upload = models.ImageField(upload_to='icon', default='icon/avatar.jpg/', verbose_name='头像',max_length=512)
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')

    objects = UserProfileManager()
    REQUIRED_FIELDS = ['email', 'name', 'mobile',]

    def get_full_name(self):
        return self.name

    def get_account_id(self):
        return self.user_id

    def __str__(self):
        return '%s-%s-%s' % (self.user_id,self.email,self.mobile)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def roles(self):
    #     role_list = Role.objects.all()
    #     roles =[role.name for role in role_list]
    #     return roles

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table = table_prefix + "user"
        verbose_name_plural = "用户信息表"



class Role(models.Model):
    _id = models.CharField(max_length=64, auto_created=True, primary_key=True, default=UUIDTools.uuid4_hex, verbose_name="UID")
    name = models.CharField(max_length=64, unique=True, verbose_name='角色名称')
    describe = models.CharField(max_length=128, null=True,blank=True, verbose_name='描述信息')
    statue_choice = (
        (0, "作废"),
        (1, "有效"),
    )
    statue = models.SmallIntegerField(choices=statue_choice, default=1, verbose_name="状态")
    menu = models.ManyToManyField('Menu', verbose_name='拥有菜单')
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    class Meta:
        db_table = table_prefix + "role"
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.name


class Menu(BaseModel):
    rid = models.AutoField(primary_key=True)
    name = models.CharField('菜单名称',unique=True, max_length=64)
    title = models.CharField('菜单标题',unique=True, max_length=64)
    icon = models.CharField('图标',default='SetUp', max_length=64)
    pid = models.SmallIntegerField('父级菜单',default=0)
    path = models.CharField(max_length=128, verbose_name='菜单路径')
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')

    def __str__(self):
        return self.name

    class Meta:
        db_table = table_prefix + "menu"
        verbose_name_plural = "菜单"
