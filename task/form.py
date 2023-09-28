from django import forms
from . models import Task, TaskImage

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['is_complete'].required = False
        
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
     
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Enter title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Type here'}))
    due_date=forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date'}))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    is_complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    #created_at = forms.DateTimeField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']
        
    

class TaskImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = TaskImage
        fields = ['image']
    
    
