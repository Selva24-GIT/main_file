from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def add_Students(requset):
    if requset.method == 'POST':
        title = requset.POST['title']
        des = requset.POST.get('des')

        Taskmodel.objects.create(
            title=title,
            des=des
        )
        print(requset.POST)
        return redirect('Students list')
            
    
    return render(requset,"add_Students.html")

def Students_list(request):
    data = Taskmodel.objects.all() 
    return render(request,"index.html",{'data':data})


def complete_u(request,pk):
    data = Taskmodel.objects.get(id=pk)
    completemodel.objects.create(
        title = data.title,
        des = data.des
    ) 
    data.delete()
    return redirect('complete')
    
def complete(request):
    data=completemodel.objects.all()
    return render(request,"complete.html",{'data':data})



def delete_u(request,pk):
    data = Taskmodel.objects.get(id=pk)
    deletemodel.objects.create(
        title = data.title,
        des = data.des
    ) 
    data.delete()
    return redirect('delete')
    
def delete(request):
    data=deletemodel.objects.all()
    return render(request,"delete.html",{'data':data})

def delete_uc(request,pk):
    data = completemodel.objects.get(id=pk)
    deletemodel.objects.create(
        title = data.title,
        des = data.des
    ) 
    data.delete()
    return redirect('delete')

def restore_t(request,pk):
    data = deletemodel.objects.get(id=pk)
    Taskmodel.objects.create(
        title = data.title,
        des = data.des
    ) 
    data.delete()
    return redirect('restore')

def restore_uc(request,pk):
    data = completemodel.objects.get(id=pk)
    Taskmodel.objects.create(
        title = data.title,
        des = data.des
    ) 
    data.delete()
    return redirect('restore')
    
def restore(request):
    data=Taskmodel.objects.all()
    return render(request,"index.html",{'data':data})


def update(requset,pk):
    if requset.method == 'POST':
      Taskmodel.objects.filter(id=pk).update(
        title = requset.POST['title'],
        des = requset.POST.get('des')
        )
      return redirect('Students list')
            
    return render(requset,"update.html")

def deletepermanently_t(request,pk):
    data = deletemodel.objects.get(id=pk)
    data.delete()
    return redirect('delete')