# salary/utils.py

import datetime
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import Payroll, SalaryStructure, Deduction

# class PayrollProcessor:
#     def __init__(self, employee, month=None):
#         self.employee = employee
#         self.month = month or datetime.date.today().replace(day=1)
    
#     def generate_payroll(self):
#         try:
#             salary_structure = SalaryStructure.objects.get(employee=self.employee)
#         except ObjectDoesNotExist:
#             raise ValueError("Salary structure not defined for this employee.")
        
#         # Fetch deductions for the given month
#         deductions = Deduction.objects.filter(
#             employee=self.employee,
#             date__month=self.month.month,
#             date__year=self.month.year
#         )
#         total_deductions = sum(d.amount for d in deductions)
        
#         gross_salary = salary_structure.basic + salary_structure.allowances
#         net_salary = gross_salary - total_deductions

#         # Prevent duplicates
#         if Payroll.objects.filter(employee=self.employee, month=self.month).exists():
#             raise ValueError("Payroll already exists for this employee for the given month.")

#         with transaction.atomic():
#             payroll = Payroll.objects.create(
#                 employee=self.employee,
#                 month=self.month,
#                 gross_salary=gross_salary,
#                 net_salary=net_salary,
#                 status='pending'
#             )
#             for deduction in deductions:
#                 payroll.deductions.add(deduction)

#         return payroll


class PayrollProcessor:
    def __init__(self, employee, month):
        self.employee = employee
        self.month = month

    def generate_payroll(self):
        # Logic to calculate and generate payroll
        # For example:
        salary_structure = self.employee.salary_structure
        deductions = Deduction.objects.filter(employee=self.employee)
        gross_salary = salary_structure.total_gross()
        total_deductions = sum(deduction.amount for deduction in deductions)
        net_salary = gross_salary - total_deductions

        payroll = Payroll.objects.create(
            employee=self.employee,
            month=self.month,
            gross_salary=gross_salary,
            total_deductions=total_deductions,
            net_salary=net_salary,
            payment_method="Bank Transfer",  # Example
            bank_account="IBAN123456",  # Example
            status="draft",
        )

        return payroll
