from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
        
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number',
                'max_length': 10
            }),

            'department': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter Department'
            }),
        
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }),
            'userId': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Id'
            }),
        }
