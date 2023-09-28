from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . form import  TaskForm, TaskImageForm
# from django.forms import formset_factory
from django.forms import modelformset_factory
from . models import Task, TaskImage

# Create your views here.
class AllTaskView(TemplateView):
    template_name = 'task/showTask.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.all()
        context = {'task':task}
        return context
    

class AddTaskView(TemplateView):
    template_name = "task/addTask.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = TaskForm()
        #ImageFormSet  = modelformset_factory(TaskImage, form=TaskImageForm, extra=10)
        # formset = ImageFormSet(queryset=Images.objects.none())
        context = {'fm':fm}
        return context
    
    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        
        if task_form.is_valid():
            task = task_form.save()  # Create the Task

            # Process the uploaded images and create TaskImage instances
            for image in request.FILES.getlist('image'):
                task_image = TaskImage(task=task, image=image)
                task_image.save()

            return HttpResponse('Data saved successfully.')

        return HttpResponse('Error in form submission.')
    