from django.db import models

# Create your models here.
class LoginModel(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)