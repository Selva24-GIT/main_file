from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    data=indiaStateCapital.objects.all()
    return render(request,'index.html',{'data':data})

def add_information(request):

    if request.method == 'POST':
        State = request.POST['state']
        Capital = request.POST['capital']

        indiaStateCapital.objects.create(
            State=State,
            Capital=Capital
        )
        return redirect('index')

    
    return render(request,'add.html')



    
    
    