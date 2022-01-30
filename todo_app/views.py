from django.shortcuts import render
from .models import Todo
# Create your views here.

# Не забыть протестить русский язык в HTML


def show_all_days(request):
    return render(request, 'todo_app/all_days.html')


def show_one_day(request):
    return render(request, 'todo_app/one_day.html')


def show_calendar(request):
    pass


