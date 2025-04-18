from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class SalaryStructure(models.Model):
    employee = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='salary_structure'
    )
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    transport_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def total_gross(self):
        return(self.base_salary + self.housing_allowance + self.transport_allowance + self.medical_allowance)

    def __str__(self):
        return f"{self.employee.get_full_name()} - Salary Structure"

class Deduction(models.Model):
    DEDUCTION_TYPES = [
        ('tax', 'Income Tax'),
        ('ss', 'Social Security'),
        ('loan', 'Loan'),
        ('other', 'Other')
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    deduction_type = models.CharField(max_length=20, choices=DEDUCTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_deduction_type_display()} - {self.amount} ({self.employee.get_full_name()})"

class Payroll(models.Model):
    PAYROLL_STATUS = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('processed', 'Processed'),
        ('paid', 'Paid')
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2)
    total_deductions = models.DecimalField(max_digits=12, decimal_places=2)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=34)  # IBAN compliant
    status = models.CharField(max_length=20, choices=PAYROLL_STATUS, default='draft')
    processed_at = models.DateTimeField(null=True, blank=True)
    deductions = models.ManyToManyField(Deduction, blank=True)

    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.month.strftime('%B %Y')}"

    class Meta:
        unique_together = ('employee', 'month')


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.action} - {self.model} - {self.created_at}"


class Department(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


