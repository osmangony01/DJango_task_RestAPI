
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTaskView.as_view(), name='home'),
    path('add/', views.AddTaskView.as_view(), name='add-task'),
    path('edit/<int:pk>', views.EditTaskView.as_view(), name='edit-task'),
    path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='delete-task'),
    path('details/<int:pk>', views.DetailsTaskView.as_view(), name='details-task'),
]