from django.shortcuts import render



# Create your views here.
 
def app1(request):
    return render(request,"main.html")