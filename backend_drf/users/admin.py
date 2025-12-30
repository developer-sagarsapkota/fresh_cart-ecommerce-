from django.contrib import admin
from .models import User
# Using alias as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    fieldsets = ()

# Register your models here.
admin.site.register(User, UserAdmin)
