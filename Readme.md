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