from django.urls import path
from .views import *

urlpatterns = [
    path('', Students_list, name='Students list'),
    path('add Students', add_Students, name='add_Students' ),
    path('complete', complete, name='complete'),
    path('delete', delete, name='delete'),
    path('restore', restore, name='restore'),

    path('c_h/<int:pk>',complete_u, name='c_h'),
    path('d_h/<int:pk>',delete_u, name='d_h'),

    path('r_hc/<int:pk>',restore_uc, name='r_hc'),
    path('d_hc/<int:pk>',delete_uc, name='d_hc'),

    path('r_ht/<int:pk>',restore_t, name='r_ht'),
    path('d_ht/<int:pk>',deletepermanently_t, name='d_ht'),

    path('update/<int:pk>', update, name='update')
    
]
