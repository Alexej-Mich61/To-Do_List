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

в settings.py изменил часовой пояс `TIME_ZONE = 'Europe/Moscow'`

### создал папку  `templates` в приложении `todos`. в ней нй еще одну папку `todos` для шаблонов

Сделал
`python manage.py makemigrations` 
`python manage.py migrate` 

Создал админа:
`python manage.py createsuperuser`
в админке создал еще юзера "модератор"

### Первый функционал:
- В todos/models.py, сделал модель Task
- В todos/forms.py, создал форму для модели Task
- В todos/views.py, создал представления для списка, создания, обновления и удаления 
задач (декораторы)
- Создал шаблоны для списка задач, формы задачи 
и подтверждения удаления задачи в todos/templates/todos/:
task_list.html, task_form.html, task_confirm_delete.html, 
- В todos/urls.py, определил URL-паттерны для представлений
- В todo/urls.py, включил URL-паттерны из todos/urls.py:
Сделал миграцию
Обновил task_list.html, чтобы добавить три строки:
- Приветствие   пользователя
- Количество задач
- Количество пользователей
в верхней части страницы и обернул каждую задачу в контейнер HTML.
В todos/views.py, обновил представление task_list, чтобы передать
количество пользователей в контекст шаблона

