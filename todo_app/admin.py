from django.contrib import admin
from . models import Todo
# Register your models here.

@admin.register(Todo) # or admin.site.register(Tod o, TodoAdmin)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['day', 'deadline', 'task']
    list_editable = ['task', 'deadline']
    ordering = ['deadline']
    list_per_page = 7
