from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User # 이 때만 models에 있는 유저 가져온다.
# Register your models here.

admin.site.register(User, UserAdmin)
