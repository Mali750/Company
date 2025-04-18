from django import forms
from .models import Staff, LoginModel


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

#for login form
class LoginForm(forms.ModelForm):
    userId = forms.CharField(
        label= 'User Id',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User ID'})
    )
    password = forms.CharField(
        label= 'Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )

    class Meta:
        model = LoginModel
        fields = ['userId', 'password']