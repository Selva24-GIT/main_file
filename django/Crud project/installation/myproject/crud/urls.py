from django.urls import path
from .views import *

urlpatterns = [
    path('Students list', crud, name='Students list'),
    path('add Students', add_Students, name='add_Students' )
]
