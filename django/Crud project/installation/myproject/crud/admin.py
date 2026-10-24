from django.contrib import admin
from .models import *
# Register your models here.
 

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display =('id','name','course','age')
    search_fields = ('name','course','id')
    list_filter = ('course','age')
    ordering = ('id',)

admin.site.register(Taskmodel)
admin.site.register(completemodel)
admin.site.register(deletemodel)