from django.db import models

# Create your models here.
class indiaStateCapital(models.Model):
    State=models.CharField(max_length=50)
    Capital=models.CharField(max_length=50)

    