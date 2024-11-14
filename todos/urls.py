# todos/urls.py
# префикс будет в urlах /todos/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('buildings/', views.building_list, name='building_list'),
    path('buildings/new/', views.building_create, name='building_create'),
    path('buildings/<int:pk>/edit/', views.building_update, name='building_update'),
    path('buildings/<int:pk>/delete/', views.building_delete, name='building_delete'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('users/', views.users_list, name='users_list'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('building_search/', views.building_search, name='building_search'),
    path('task/<int:task_id>/commentary/new/', views.commentary_create, name='commentary_create'),
    path('commentary/<int:pk>/edit/', views.commentary_update, name='commentary_update'),
    path('commentary/<int:pk>/delete/', views.commentary_delete, name='commentary_delete'),
    path('task_list_active/', views.task_list_active, name='task_list_active'),
    path('task_list_completed/', views.task_list_completed, name='task_list_completed'),
]

