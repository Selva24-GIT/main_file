from django.shortcuts import render
from django.http import HttpResponse
from .models import Student



def crud(request):
    data = Student.objects.all() 
    return render(request,"index.html",{'data':data})


  