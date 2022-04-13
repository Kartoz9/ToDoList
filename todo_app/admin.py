from django.contrib import admin
from . models import Todo
# Register your models here.


@admin.register(Todo)  # or admin.site.register(T odo, TodoAdmin)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['day', 'date', 'task']
    list_editable = ['task']
    ordering = ['date']
    list_per_page = 7
