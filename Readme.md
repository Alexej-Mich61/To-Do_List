# Учебный проект To-Do_List
- репозиторий
- проект To-Do_list
- установка зависимостей `pip install django==4.2`
- запись зависимостей в файл `requirements.txt` командой `pip freeze > requirements.txt`
развернуть проект на локальной машине
- склонировать репозиторий командой `git clone`
- перейти в папку проекта `cd To-Do_List`
- создать виртуальное окружение `python -m venv venv`
- активировать окружение `source venv/bin/activate`
- установить зависимости `pip install -r requirements.txt`

# Создание Django project
- создать проект `django-admin startproject todo .` (точка через пробел 
создает проект в текущей директории)
- запуск проекта `python manage.py runserver` (на одном уровне с manage.py)
остановка сервера - `Ctrl+C`

*******Команды терминала****** 
- `python manage.py runserver` запуск сервера
- `cd` смена директории
- `cd..` подняться на 1 уровень выше
- `ls` просмотр содержимого директории
- `pwd` показать текущую директорию

# Создание приложения `python manage.py startapp todos`
После регистрируем в файле `settings.py` в разделе `INSTALLED_APPS`
'todos' # добавляем приложение todos в список последним
чтобы приложение работало

### первое представление
```python
from django.http import HttpResponse

def main(request):
    return HttpResponse("Привет, мир!")
```
регистрируем приложение в файле `urls.py` приложения

### Первый url
```python
 path('', views.main),
```
страничка возвращает привет мир

### Детальное представление карточки по ID
Делаем новый маршрут с конвертом int, который будет принимать ID карточки в урл
```python
path('tasks/<int:task_id>/', views.task_by_id, name='task_details'),
```
И функцию, которая обрабатывает запрос и возвращает страницу с детальной информацией о карточке
```python
def task_by_id(request, task_id):
    return HttpResponse(f"Вы открыли задачу {task_id}")
```
### include и собственный файл `url.py` для приложения `todos`
- еще одно представление `get_all_tasks` в url.py
- новый файл `urls.py` в директории приложения todos
- регистрируем с помощью include
- маршруты без префиксов в файле url.py приложения
- удалил маршруты `tasks/` из файла  urls.py конфигурации проекта