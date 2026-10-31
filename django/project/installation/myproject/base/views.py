from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.decorators import login_required
from .models import *



# Create your views here.
def register(request):
   if request.user.is_authenticated:
      return redirect('profile_view')
   
   if request.method == 'POST':
      print(request.POST)
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request,user)
         return redirect('profile_view')
      else:
         print("not valid")
   else:
      form = UserCreationForm()
   return render(request, "register.html", {'form':form})



def login_view(request):
    if request.user.is_authenticated:
         return redirect('profile_view')
    error = ""

    if request.method == 'POST':
      username = request.POST.get('username')
      userpassword =  request.POST.get('userpassword')
      user = authenticate(
         request,
         username = username,
         userpassword = userpassword 
      )
      if user is not None:
        login(request,user)
        return redirect('profile_view')
      else:
         error = "invalid usename or password."


    return render(request,'login.html', {'error':error})


@login_required
def profile_view(request):
   return render(request,'profile.html')
def logout_view(request):
   if request.method == 'POST':
      logout(request)
      return redirect('login_view')
   
   return render(request,'profile.html')