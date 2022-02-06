from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_days, name='menu'),
    path('diary/<int:id_todo>', views.show_one_day, name='one-day'),
    path('diary/<int:id_todo>/leave_task', views.leave_task, name='leave-task'),
    path('calendar', views.show_calendar, name='calendar')
]