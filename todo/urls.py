"""
URL configuration for todo project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Добавьте этот импорт
# from todos import views


# Подключаем файл urls.py из приложения todos через include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Включите встроенные представления аутентификации Django
    path('', include('todos.urls')), # Включаем URL для приложения todos
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Добавьте этот маршрут
]

