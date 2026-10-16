from django.urls import path
from .views import app1


urlpatterns = [
    path('main/', app1, name='main')
   
 ]