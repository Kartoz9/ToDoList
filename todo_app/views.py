from django.shortcuts import render
from .models import Todo
# Create your views here.

# Не забыть протестить русский язык в HTML


def show_all_days(request):
    todo = Todo.objects.all()
    return render(request, 'todo_app/all_days.html', {
        'todo': todo,
    })


def show_one_day(request, day_todo: str):
    example = Todo.objects.get(day=day_todo)
    return render(request, 'todo_app/one_day.html', {
        'example': example,
    })


def show_calendar(request):
    pass


