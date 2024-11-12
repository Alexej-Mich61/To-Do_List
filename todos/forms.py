from django import forms
from .models import Task, Building, Commentary

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'building', 'status']

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['ak', 'building_name', 'address']

class BuildingSearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['text']
