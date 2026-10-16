from django.urls import path
from .views import demo, abt, product


urlpatterns = [
    path('abt/', abt, name='abt'),
    path('p/<int:id>/', product, name='product'),
    path('d/<int:id>/', demo, name='demo'),

   
 ]