from django.urls import path
from .views import *

urlpatterns = [
    path('register',register,name='register'),
    path('login_view',login_view, name='login_view'),
    path('profile_view',profile_view, name='profile_view'),
    path('logout_view',logout_view, name="logout_view")
]