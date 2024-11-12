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

### Создал шаблоны, добавил модель building
- добавил базовый шаблон, меню в него и расширил его другими шаблонами

### Установил отношения Task с моделью Building. 
- `building = models.ForeignKey('Building', on_delete=models.SET_NULL, null=True, blank=True)`
- на страницах Create Task и Edit Task под полем Description появилась ссылка add building 
to task, по нажатию на которое открывалось окно с строкой поиска для ввода текста 
и кнопкой найти. поиск должен производиться в building по всем трем полям 
(building.ak, building.address, building_name), В окне поиска должны 
выводиться списком building с найденными результатами. Пользователь должен 
будет выбрать нужный ему building из списка, выделить его нажатием курсора 
и нажать кнопку добавить. После этого вернуться на предыдущую страницу  
(Create Task или Edit Task). Привязанный building должен там отображаться 
под строкой Description. также там должна быть кнопка удаления building из 
Task.  В Task List привязанный building должен отображаться под полем Description. 
Отношения между building и task нужно установить таком образом, чтобы при 
удалении task не удалялся building из базы и Building List, и при удалении 
building не удалялся task, а только исчезала запись о привязанном building. 
Привязка building к task должно - необязательное поле

- выполнил миграцию

### комит
Изменил код так: добавил в Building Search и в Task List в строках Building: отображение 
поля AK перед building Name, также к task добавил свойство status, которое может быть 
active или completed и которое можно выбирать из выпадающего списка. 
По умолчанию при создании задачи должен назначаться status - active, 
в Task List поля task должны отображаться в следующей последовательности: 
Title,  Description, Building, Assigned to, Created at, Status, 
После этого ссылки изменения и удаления задачи

#### Миграция

### Добавил модель комментария, установил отношения между Task и Commentary. 
- в тексте комментария добавил предзаполненный текст
- автоматическую установку даты и времени при создании
- выполнил миграцию
