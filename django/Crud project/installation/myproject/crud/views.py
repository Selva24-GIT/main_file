from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def crud(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")