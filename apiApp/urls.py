from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api'),
    path('task/', views.TaskList.as_view()),
    path('task/<int:pk>/', views.TaskDetail.as_view()),
    path('taskImage/', views.TaskImageList.as_view()),
   
]