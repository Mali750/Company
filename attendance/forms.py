from django import forms
from .models import Employee

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'fingerprint_hash', 'rfid_tag']  # Customize as needed


        widgets = {
        'department': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Department',
        }),
        'fingerprint_hash': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'fingerprint',
        }),
        'rfid_tag': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'rfid',
        }),

        }
