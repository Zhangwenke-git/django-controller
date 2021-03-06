from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.safestring import mark_safe


class UserProfileManager(BaseUserManager):
    def create_user(self, user_id, password, email, name,mobile):
        if not user_id:
            raise ValueError('User must have an account id!')
        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            name=name,
            mobile=mobile
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email, name,mobile):
        user = self.create_user(
            user_id=user_id,
            password=password,
            email=email,
            name=name,
            mobile=mobile
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = 1
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
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

    statue_choice = (
        (0, "否"),
        (1, "是"),
    )
    is_active = models.SmallIntegerField(choices=statue_choice, default=1, verbose_name="活动状态")
    sex_choice = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )
    sex = models.SmallIntegerField(choices=sex_choice, default=2, verbose_name="性别")

    role = models.ManyToManyField('Role', blank=True, null=True, verbose_name='角色')
    upload = models.ImageField(upload_to='icon', default='icon/default.png', verbose_name='头像')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

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

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = "用户信息表"

from django.contrib.auth.models import Group


class Groups(Group):
    description = models.CharField(max_length=320, null=True, blank=True, verbose_name='描述')

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = '权限组'


class Role(models.Model):
    rolename = models.CharField(max_length=64, unique=True, verbose_name='角色名称')
    statue_choice = (
        (0, "作废"),
        (1, "有效"),
    )
    statue = models.SmallIntegerField(choices=statue_choice, default=1, verbose_name="状态")
    menus = models.ManyToManyField('FirstLayerMenu', verbose_name='一层菜单', blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.rolename


class FirstLayerMenu(models.Model):
    type_choice = (
        (0, "api"),
        (1, "public"),
    )
    type = models.SmallIntegerField(choices=type_choice, default=1, verbose_name="类型")
    name = models.CharField('一层菜单名', max_length=64)
    icon = models.CharField('图标', default=mark_safe("glyphicon glyphicon-blackboard"), max_length=64)
    url_type_choices = ((0, '相关的名字'), (1, '固定的URL'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0, verbose_name="URL类型")
    url_name = models.CharField(max_length=64, verbose_name='一层菜单路径')
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')
    sub_menus = models.ManyToManyField('SubMenu', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = "第一层菜单"


class SubMenu(models.Model):
    '''第二层侧边栏菜单'''
    name = models.CharField('二层菜单名', max_length=64)
    url_type_choices = ((0, '相关的名字'), (1, '固定的URL'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0, verbose_name="URL类型")
    url_name = models.CharField(max_length=64, verbose_name='二层菜单路径')
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = "第二层菜单"
