from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def show_calendar(request):      #<img src='{% static "todo_app/img/calendar.png"%}' width = "25px" height="25">
    return render(request, 'todo_app/calendar.html')


class HomeListView(ListView):   #<img src='{% static "todo_app/img/main.png"%}' width = "25px" height="25">
    model = Todo
    template_name = 'todo_app/all_days.html'
    context_object_name = 'todo'


class DetailView(DetailView):
    model = Todo
    template_name = 'todo_app/one_day.html'
    context_object_name = 'example'


class CustomSuccessMessageMixin:

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class TodoCreateViews(CustomSuccessMessageMixin, CreateView):
    model = Todo
    template_name = 'todo_app/edit_page.html'
    form_class = TodoForm
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка создана'

    def get_context_data(self, **kwargs):
        kwargs['example'] = Todo.objects.all().order_by('id')
        return super().get_context_data(**kwargs)


class TodoUpdateView(CustomSuccessMessageMixin, UpdateView):
    model = Todo
    template_name = 'todo_app/edit_page.html'
    form_class = TodoForm
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_app/edit_page.html'
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

