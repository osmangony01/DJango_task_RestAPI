from rest_framework import serializers
from task.models import Task, TaskImage
from django.utils import timezone
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'due_date', 'priority', 'is_complete', 'uname']
    
    
class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ['id','task_id', 'image',]    
    
    