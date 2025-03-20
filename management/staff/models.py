from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.hashers import make_password


# # Create your models here.
# class Staff(models.Model):
#     name = models.CharField(_("Name"), max_length=50)
#     email = models.EmailField(_("Email Address"), max_length=254, unique=True, blank=True)  # Remove null=True
#     mobile = PhoneNumberField(_("Mobile Number"), region='IN', unique=True, blank=True, null=True)  # PhoneNumberField can store NULL
#     department = models.CharField(_("Department"), max_length=50, blank=True)  # Remove null=True
#     userId = models.CharField(_("User_Id"), max_length=50, blank=True)  # Remove null=True
#     password = models.CharField(_("Password"), max_length=128, blank=True)  # Remove null=True


            
#     def __str__(self):
#         return self.name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class StaffManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Staff(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email Address"), unique=True)
    mobile = PhoneNumberField(_("Mobile Number"), region='IN', unique=True, blank=True, null=True)
    department = models.CharField(_("Department"), max_length=50, blank=True)
    userId = models.CharField(_("User ID"), max_length=50, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = StaffManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

