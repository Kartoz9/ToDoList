from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='menu'),
    path('diary/<int:pk>', views.DetailView.as_view(), name='one-day'), #pk тоже самое что и id
    path('calendar', views.show_calendar, name='calendar'),
    path('edit-page', views.edit_page, name='edit-page')
]