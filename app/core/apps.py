from core import models
from django.apps import AppConfig
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


class CoreConfig(AppConfig):
    name = 'core'


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)





