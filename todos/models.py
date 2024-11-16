# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False) # по дефолту не одобренный администратором

class Building(models.Model): # объекты/здания
    ak = models.CharField(max_length=100)
    building_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ak}. {self.building_name}"

class Task(models.Model): # задачи
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey('todos.CustomUser', on_delete=models.CASCADE, null=True, blank=True) # один ко многим
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True, blank=True) # один ко многим
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title

class Commentary(models.Model): # комментарии
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='commentaries') # один ко многим
    user = models.ForeignKey('todos.CustomUser', on_delete=models.CASCADE) # один ко многим
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
