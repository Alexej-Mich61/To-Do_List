from django import forms
from .models import Task, Building

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to']

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['ak', 'building_name', 'address']