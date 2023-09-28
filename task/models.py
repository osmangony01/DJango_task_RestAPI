from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=200, blank=True)
    #description = models.TextField(blank=True)

class TaskImage(models.Model):
	task = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="", blank=True)
