from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import aauthenticate,login
from django.contrib.auth.forms import UserCreationForm  
from .models import *



# Create your views here.
def register(request):
   if request.user.is_authenticated:
      return redirect('profile')


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
      
        return redirect('')
    else:
       return render(request,  )

    return render(request,'login.html')