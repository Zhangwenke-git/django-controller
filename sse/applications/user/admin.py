from django.contrib import admin

# Register your models here.

# Register your models here.
from user.models import UserProfile,Role,Menu
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Menu)