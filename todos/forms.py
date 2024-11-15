# form.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser, Task, Building, Commentary

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

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
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Выполнено'}),
        }

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2 = forms.CharField(label="Confirm new password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))
