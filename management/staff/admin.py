from django.contrib import admin
from .models import Staff

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'department', 'userId', 'password')