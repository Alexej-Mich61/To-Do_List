from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Building(models.Model):
    ak = models.CharField(max_length=100)
    building_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.building_name
