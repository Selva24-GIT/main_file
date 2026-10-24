from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data=india.objects.all()
    return render(request,'index.html',{'data':data})

def add(request):
     if request.method=='POST':
        State=request.POST['State']
        capital=request.POST['capital']
        india.objects.create(
            State=State,
            capital=capital)
        return redirect(request,'index.html')

     return render(request,'add.html')
