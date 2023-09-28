from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View, RedirectView
from . form import  TaskForm, TaskImageForm
# from django.forms import formset_factory
from django.forms import modelformset_factory
from . models import Task, TaskImage
from datetime import date, datetime
import json
from django.contrib.auth.decorators import login_required

# @login_required(login_url="login")

# Create your views here.
class AllTaskView(TemplateView):
    template_name = 'task/showTask.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.all()
        print(task)
        context = {'task':task}
        return context
    
    def post(self, request, *args, **kwargs):
        
        search_title = request.POST.get('search_title', '') 
        if search_title:
            tasks = Task.objects.filter(title__icontains=search_title)
            print('search :: '+search_title)
        else:
            #tasks = Task.objects.all()
            
            creation_date = request.POST.get('creation_date', '')
            due_date = request.POST.get('due_date', '')
            priority = request.POST.get('priority', '')
            is_complete = request.POST.get('mark', '')
            
            # print(creation_date, due_date, priority, is_complete)
            
            
          
            # Start with all tasks
            tasks = Task.objects.all()

            # Apply filters based on criteria
            if creation_date:
                print('create_date :'+creation_date)
                # Filter by creation date
                input_creation_date = datetime.strptime(creation_date, '%Y-%m-%d').date()
                tasks = tasks.filter(created_at__gte=input_creation_date)

            if due_date:
                print('due date :'+ due_date)
                # Filter by due date
                input_due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
                tasks = tasks.filter(due_date__gte=input_due_date)

            if priority:
                print('priority :' +priority)
                # Filter by priority
                tasks = tasks.filter(priority__icontains=priority)

            if is_complete:
                # Filter by completion status
                print('mark :'+is_complete)
                status = json.loads(is_complete.lower())
                tasks = tasks.filter(is_complete=status)
            
                
        
        context = { 'task': tasks}
        
        return render(request, self.template_name, context)
        #return redirect('home', context)
    

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
        print(task_form)
        if task_form.is_valid():
            task = task_form.save()  # Create the Task

            # Process the uploaded images and create TaskImage instances
            for image in request.FILES.getlist('image'):
                task_image = TaskImage(task=task, image=image)
                task_image.save()

            return redirect('home')

        return HttpResponse('Error in form submission.')
    
    
class EditTaskView(View):
    #template_name = 'task/editTask.html'
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        #print(task)
        task_images = TaskImage.objects.filter(task=pk)
        #print(task_images)
        fm = TaskForm(instance=task)
        
        # for task_image in task_images:
        #     print(f"Image: {task_image.image.url}")  
        context = {'fm':fm}
        return render(request, 'task/editTask.html', context) 
    
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        fm =TaskForm(request.POST, instance=task)
        if fm.is_valid():
            fm.save()
        return redirect('home')
    
    


class DeleteTaskView(RedirectView):
    url = '/task'
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs['pk'])
        del_id = kwargs['pk']
        Task.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class DetailsTaskView(TemplateView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task_images = TaskImage.objects.filter(task=pk)
        context = {'task':task, 'images':task_images}
        return render(request, 'task/detailsTask.html', context) 

