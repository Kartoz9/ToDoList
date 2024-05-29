from django.contrib import admin
from . models import Todo


@admin.register(Todo) 
class TodoAdmin(admin.ModelAdmin):
    list_display = ['day', 'date', 'task']
    list_editable = ['task']
    ordering = ['date']
    list_per_page = 7
