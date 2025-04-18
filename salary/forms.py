from django import forms
from .models import SalaryStructure, Deduction, Payroll

class SalaryStructureForm(forms.ModelForm):
    class Meta:
        model = SalaryStructure
        fields = [
            'employee',
            'base_salary',
            'housing_allowance',
            'transport_allowance',
            'medical_allowance',
            'effective_date',
            'is_active'
        ]
        widgets = {
            'effective_date': forms.DateInput(attrs={'type': 'date'})
        }

class DeductionForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = [
            'employee',
            'deduction_type',
            'amount',
            'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = [
            'employee',
            'month',
            'gross_salary',
            'total_deductions',
            'net_salary',
            'payment_method',
            'bank_account',
            'status'
        ]
        widgets = {
            'month': forms.DateInput(attrs={'type': 'month'}),
            'bank_account': forms.TextInput(attrs={'placeholder': 'IBAN or bank account'}),
        }


