from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=10)
    department = models.CharField(max_length=300)
    userId = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



# for login 
class LoginModel(models.Model):
    userId = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.userId
