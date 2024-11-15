from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)

class Building(models.Model):
    ak = models.CharField(max_length=100)
    building_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ak}. {self.building_name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey('todos.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title

class Commentary(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='commentaries')
    user = models.ForeignKey('todos.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
