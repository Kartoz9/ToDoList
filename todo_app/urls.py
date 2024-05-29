from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='menu'),
    path('diary/<int:pk>', views.DetailPageView.as_view(), name='one-day'), 
    path('calendar', views.show_calendar, name='calendar'),
    path('edit-page', views.TodoCreateView.as_view(), name='edit-page'),
    path('update-page/<int:pk>', views.TodoUpdateView.as_view(), name='update-page'),
    path('delete-page/<int:pk>', views.TodoDeleteView.as_view(), name='delete-page'),
    path('login', views.MyprojectLoginView.as_view(), name='login-page'),
    path('register', views.RegisterUserView.as_view(), name='register-page'),
    path('logout', views.MyprojectLogOut.as_view(), name='logout-page'),

]