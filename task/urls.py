
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='signin'),
    #path('', '', name='signup'),
    # path('', include('employee.urls')),
]