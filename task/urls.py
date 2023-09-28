
from django.urls import path
from . import views
from .views import AllTaskView
from django.contrib.auth.decorators import login_required

 
urlpatterns = [
    path('', login_required(AllTaskView.as_view()), name='home'),
    path('add/', views.AddTaskView.as_view(), name='add-task'),
    path('edit/<int:pk>', views.EditTaskView.as_view(), name='edit-task'),
    path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='delete-task'),
    path('details/<int:pk>', views.DetailsTaskView.as_view(), name='details-task'),
]