from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login
from .models import Todo
from .forms import TodoForm, AuthUserForm, RegisterUserForm


def show_calendar(request):
    return render(request, 'todo_app/calendar.html')


class HomeListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login-page')
    model = Todo
    template_name = 'todo_app/all_days.html'
    queryset = Todo.objects.all().order_by('date')
    context_object_name = 'tasks'


class DetailPageView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login-page')
    model = Todo
    template_name = 'todo_app/one_day.html'
    context_object_name = 'task'


class CustomSuccessMessageMixin:

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class TodoCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login-page')
    model = Todo
    template_name = 'todo_app/edit_page.html'
    form_class = TodoForm
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка создана'

    queryset = Todo.objects.all().order_by('date')
    context_object_name = 'tasks'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Todo
    template_name = 'todo_app/edit_page.html'
    form_class = TodoForm
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

class MyprojectLoginView(LoginView):
    template_name = 'todo_app/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('menu')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = Todo
    template_name = 'todo_app/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('menu')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class MyprojectLogOut(LogoutView):
    next_page = reverse_lazy('edit-page')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_app/edit_page.html'
    success_url = reverse_lazy('edit-page')
    success_msg = 'Заметка удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)