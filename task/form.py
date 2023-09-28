from django import forms
from . models import Task, TaskImage
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['title']
        
    

class TaskImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = TaskImage
        fields = ['image']
    
    
