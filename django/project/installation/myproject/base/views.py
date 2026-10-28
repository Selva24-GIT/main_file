from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import aauthenticate,login
from django.contrib.auth.forms import UserCreationForm  
from .models import *



# Create your views here.
def index(request):
    data = LoginModel.objects.all()
    return render(request,'index.html',{'data':data})

def login(request):
    if request.method == 'POST':
      username = request.POST['username']
      userpassword =  request.POST['userpassword']

      user = aauthenticate(
         request,
         username = username,
         userpassword = userpassword 
      )
      if user is not None:
        login(request,user)
      
        return redirect('index')
    else:
       return render(request,  )

    return render(request,'login.html')