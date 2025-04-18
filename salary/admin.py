from django.contrib import admin
from .models import SalaryStructure, Deduction, Payroll

@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):
    list_display = ('employee', 'base_salary', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('employee__username',)
    raw_id_fields = ('employee',)

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('month', 'employee', 'net_salary', 'status')
    list_filter = ('status', 'month')
    search_fields = ('employee__username',)
    actions = ['process_payments']
    
    def process_payments(self, request, queryset):
        # Implement bulk payment processing
        pass