from django.shortcuts import render, redirect
from .models import Todo
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import TodoForm


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


@csrf_exempt
def edit_page(request):
    success = False
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    example = Todo.objects.all().order_by('id')
    template = 'todo_app/edit_page.html'
    context = {
        'example': example,
        'form': TodoForm(),
        'success': success
    }
    return render(request, template, context)


@csrf_exempt
def update_page(request, pk):
    get_todo = Todo.objects.get(pk=pk)
    success_update = False
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=get_todo)
        if form.is_valid():
            form.save()
            success_update = True

    template = 'todo_app/edit_page.html'
    context = {
        'get_todo': get_todo,
        'update': True,
        'form': TodoForm(instance=get_todo),
        'success_update': success_update
    }
    return render(request, template, context)


def delete_page(request, pk):
    get_todo = Todo.objects.get(pk=pk)
    get_todo.delete()
    return redirect(reverse('edit-page'))
