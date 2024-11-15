# admin.py
from django.contrib import admin
from .models import CustomUser, Building, Task, Commentary

admin.site.register(CustomUser)
admin.site.register(Building)
admin.site.register(Task)
admin.site.register(Commentary)
