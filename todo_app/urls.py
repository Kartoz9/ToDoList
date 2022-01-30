from django.urls import path
from . import views

urlpatterns = [
    path('diary/', views.show_all_days),

]