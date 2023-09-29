from django.db import models
from django.utils import timezone
from datetime import date

class Task(models.Model):
    
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    due_date = models.DateField(default=date.today)
    priority = models.CharField(max_length=10, default='Medium')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super(Task, self).save(*args, **kwargs)

class TaskImage(models.Model):
    task = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", blank=True)
    