from django.db import models

# Create your models here.
class india(models.Model):
    State=models.CharField(max_length=100)
    capital=models.CharField(max_length=100)