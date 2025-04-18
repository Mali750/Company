
from django.urls import path
from .views import (
    PayrollListView,
    GeneratePayrollView,
    ApprovePayrollView,
    DeductionCreateView,
    EmployeeDeductionListView,
    SalaryStructureUpdateView,
    EmployeeSalaryDetailView,
    SalaryReportView,
)

app_name = 'salary'

urlpatterns = [
    path('payrolls/', PayrollListView.as_view(), name='payroll-list'),
    path('payrolls/generate/', GeneratePayrollView.as_view(), name='payroll-generate'),
    path('payrolls/approve/<int:pk>/', ApprovePayrollView.as_view(), name='payroll-approve'),

    path('deductions/create/', DeductionCreateView.as_view(), name='deduction-create'),
    path('deductions/', EmployeeDeductionListView.as_view(), name='deduction-list'),

    path('structure/update/<int:pk>/', SalaryStructureUpdateView.as_view(), name='structure-update'),
    path('structure/<int:pk>/', EmployeeSalaryDetailView.as_view(), name='employee-detail'),

    path('reports/monthly/', SalaryReportView.as_view(), name='salary-report'),
]
