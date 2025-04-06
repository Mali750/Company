from django.contrib import admin
from .models import Staff, LoginModel

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'department', 'userId', 'password')


@admin.register(LoginModel)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'password')