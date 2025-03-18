from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.hashers import make_password


# Create your models here.
class Staff(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True, blank=True)  # Remove null=True
    mobile = PhoneNumberField(_("Mobile Number"), region='IN', unique=True, blank=True, null=True)  # PhoneNumberField can store NULL
    department = models.CharField(_("Department"), max_length=50, blank=True)  # Remove null=True
    userId = models.CharField(_("User_Id"), max_length=50, blank=True)  # Remove null=True
    password = models.CharField(_("Password"), max_length=128, blank=True)  # Remove null=True


            
    def __str__(self):
        return self.name