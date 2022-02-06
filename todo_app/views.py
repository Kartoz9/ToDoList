from django.shortcuts import render
from django.http import Http404
from .models import Todo
from django.views.generic import ListView, DetailView
from django.urls import reverse
# Create your views here.


#def show_one_day(request, id_todo: int):
#    example = Tod o.objects.get(id=id_todo)
#    return render(request, 'todo_app/one_day.html', {
#        'example': example,
#    })


class HomeListView(ListView):           #<img src='{% static "todo_app/img/main.png"%}' width = "25px" height="25">
    model = Todo
    template_name = 'todo_app/all_days.html'
    context_object_name = 'todo'


class DetailView(DetailView):
    model = Todo
    template_name = 'todo_app/one_day.html'
    context_object_name = 'example'


def show_calendar(request):             #<img src='{% static "todo_app/img/calendar.png"%}' width = "25px" height="25">
    return render(request, 'todo_app/calendar.html')


def edit_page(request):
    example = Todo.objects.all().order_by('id')
    template = 'todo_app/edit_page.html'
    context = {
        'example': example
    }
    return render(request, template, context)


