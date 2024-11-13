from django.db import models
from django.contrib.auth.models import User

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
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title
