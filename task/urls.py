
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTaskView.as_view(), name='home'),
    path('add/', views.AddTaskView.as_view(), name='add-task'),
]