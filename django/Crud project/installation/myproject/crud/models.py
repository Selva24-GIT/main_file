from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return (f'{self.name} - {self.course} - {self.age}')
    

class Taskmodel(models.Model):
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
class completemodel(models.Model):
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
class deletemodel(models.Model):
    title = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    