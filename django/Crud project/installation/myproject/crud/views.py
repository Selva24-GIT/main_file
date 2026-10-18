from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student


def add_Students(requset):
    if requset.method == 'POST':
        name = requset.POST.get('name')
        course = requset.POST.get('course')
        age = requset.POST.get('age')

        Student.objects.create(
            name=name,
            course=course,
            age=int(age)
        )
        print(requset.POST)
        return redirect('Students list')
            
    
    return render(requset,"add_Students.html")

def crud(request):
    data = Student.objects.all() 
    return render(request,"index.html",{'data':data})

