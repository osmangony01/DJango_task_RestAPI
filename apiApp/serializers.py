from rest_framework import serializers
from task.models import Task, TaskImage
from django.utils import timezone
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'due_date', 'priority', 'is_complete', ]
    
    
    
class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ['id','task_id', 'image',]    
    
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # priority = serializers.CharField(allow_blank=True, max_length=10)
    # is_complete = serializers.BooleanField(required=False)
    # due_date = serializers.DateField(default=date.today)
    # description = serializers.CharField(allow_blank=True)
    # created_at = serializers.DateTimeField(default=timezone.now) 
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Task.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.priority = validated_data.get('priority', instance.priority)
    #     instance.is_complete = validated_data.get('is_complete', instance.is_complete)
    #     instance.due_date = validated_data.get('due_date', instance.due_date)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.save()
    #     return instance