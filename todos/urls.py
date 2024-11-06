from django.urls import path
from . import views
# todos/urls.py
# префикс будет в urlах /todos/

urlpatterns = [
    path('<int:task_id>/', views.task_by_id, name='task_details'),
    path('', views.get_all_tasks, name='all_tasks'),
]
