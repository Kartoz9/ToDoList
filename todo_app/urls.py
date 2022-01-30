from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_days, name='menu'),
    path('diary/<int:id_todo>', views.show_one_day, name='one-day'),
]