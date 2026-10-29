from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('add_information', add_information, name='add_information')
]