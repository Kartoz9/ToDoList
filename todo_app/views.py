from django.shortcuts import render
from django.http import Http404
from .models import Todo
from django.urls import reverse
# Create your views here.


def show_all_days(request):
    todo = Todo.objects.all()
    return render(request, 'todo_app/all_days.html', {
        'todo': todo
    })


def show_one_day(request, id_todo: int):
    example = Todo.objects.get(id=id_todo)
    return render(request, 'todo_app/one_day.html', {
        'example': example,
    })


def show_calendar(request):
    return render(request, 'todo_app/calendar.html')


def leave_task(request, id_todo: int):
    a = Todo.objects.get(id=id_todo)
    a.task_set.create(task=request.POST['text'])
    return render(request, 'todo_app/one_day.html', {
        'a': a
    })


