# Учебный проект To-Do_List (дипломная работа, группа Python-316)
- склонировать репозиторий командой `git clone` (https://github.com/Alexej-Mich61/To-Do_List)
- установка джанго `pip install django==4.2`
- установка `pip install django-debug-toolbar`
- установка `pip install python-dotenv`
- см. зависимости в файл `requirements.txt` 
- создание файла .env , заполнить переменные (какие - указаны в .env.example)
- Сделать миграцию:
`python manage.py makemigrations` 
`python manage.py migrate` 
- Создание админа:
`python manage.py createsuperuser`

1. Описание проекта
Мой проект представляет собой систему управления задачами (To-Do List) для компании, обслуживающей системы пожарной безопасности на объектах. Он включает в себя функциональность для создания, редактирования, удаления и просмотра задач, привязку объектов защиты (зданий) к задачам, адресацию выполнения задачи выбранному пользователю, а также управления пользователями и комментариями к задачам.


2. Особенности проекта
Регистрация: функционал сайта доступен пользователям только после регистрации. Регистрация пользователя требует подтверждения администратора.
Аутентификация: Пользователи могут аутентифицироваться через логин/пароль. Настроена функция сброса пароля по e-mail.
3. Интерфейс 
Меню-навигация по страницам. Список задач, список объектов, система поиска задач по заголовку, по пользователю, которому адресована задача, фильтр по статусу задач (активные, выполненные). Поиск по списку объектов (по номеру абонентского комплекта (АК), по названию.
4. Адаптивность: Bootstrap 5

5. Админ-панель: Django, группы пользователей с ограничениями доступа к функциям.

3. Технологии
Django, Bootstrap
База данных: SQLite3








