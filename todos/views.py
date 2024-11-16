# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LogoutView # для логаута
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Task, Building, Commentary, CustomUser
from .forms import TaskForm, BuildingForm, BuildingSearchForm, CommentaryForm, CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


class CustomLogoutView(LogoutView):
    next_page = 'login'  # имя URL-адреса для перенаправления после выхода

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'registration/password_reset_email.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Пользователь неактивен до подтверждения
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




@login_required
@permission_required('todos.change_customuser', raise_exception=True)
def approve_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_approved = True
    user.is_active = True  # Активируем пользователя
    user.save()
    return redirect('users_list')

@login_required
def users_list(request):
    users = CustomUser.objects.all()
    users_count = users.count()
    return render(request, 'todos/users_list.html', {'users': users, 'users_count': users_count})

# для страниц
@login_required
def task_list(request):
    search_query = request.GET.get('search')
    assigned_to_query = request.GET.get('assigned_to')
    tasks = Task.objects.all().order_by('-created_at')  # Сортировка от новой к старой

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if assigned_to_query:
        tasks = tasks.filter(assigned_to__username__icontains=assigned_to_query)

    users_count = CustomUser.objects.count()

    # Пагинация
    paginator = Paginator(tasks, 5)  # Показывать по 5 задач на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/task_list.html', {'page_obj': page_obj, 'users_count': users_count})

@login_required
def task_list_active(request):
    search_query = request.GET.get('search')
    assigned_to_query = request.GET.get('assigned_to')
    tasks = Task.objects.filter(status='active').order_by('-created_at')  # Сортировка от новой к старой

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if assigned_to_query:
        tasks = tasks.filter(assigned_to__username__icontains=assigned_to_query)

    users_count = CustomUser.objects.count()

    # Пагинация
    paginator = Paginator(tasks, 5)  # Показывать по 5 задач на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/task_list_active.html', {'page_obj': page_obj, 'users_count': users_count})

@login_required
def task_list_completed(request):
    search_query = request.GET.get('search')
    assigned_to_query = request.GET.get('assigned_to')
    tasks = Task.objects.filter(status='completed').order_by('-created_at')  # Сортировка от новой к старой

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if assigned_to_query:
        tasks = tasks.filter(assigned_to__username__icontains=assigned_to_query)

    users_count = CustomUser.objects.count()

    # Пагинация
    paginator = Paginator(tasks, 5)  # Показывать по 5 задач на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/task_list_completed.html', {'page_obj': page_obj, 'users_count': users_count})


@login_required
@permission_required('todos.add_task', raise_exception=True)
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todos/task_form.html', {'form': form})

@login_required
@permission_required('todos.change_task', raise_exception=True)
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todos/task_form.html', {'form': form})

@login_required
@permission_required('todos.delete_task', raise_exception=True)
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todos/task_confirm_delete.html', {'task': task})

@login_required
def building_list(request):
    ak_search = request.GET.get('ak_search')
    name_search = request.GET.get('name_search')
    buildings = Building.objects.all()

    if ak_search:
        buildings = buildings.filter(ak__icontains=ak_search) # поиск
    if name_search:
        buildings = buildings.filter(building_name__icontains=name_search)

    paginator = Paginator(buildings, 5)  # Показывать по 5 зданий на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/building_list.html', {'page_obj': page_obj})
@login_required
@permission_required('todos.add_building', raise_exception=True)
def building_create(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('building_list')
    else:
        form = BuildingForm()
    return render(request, 'todos/building_form.html', {'form': form})

@login_required
@permission_required('todos.change_building', raise_exception=True)
def building_update(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect('building_list')
    else:
        form = BuildingForm(instance=building)
    return render(request, 'todos/building_form.html', {'form': form})

@login_required
@permission_required('todos.delete_building', raise_exception=True)
def building_delete(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.delete()
        return redirect('building_list')
    return render(request, 'todos/building_confirm_delete.html', {'building': building})

@login_required
def about(request):
    return render(request, 'todos/about.html')

@login_required
def personal_account(request):
    return render(request, 'todos/personal_account.html', {'user': request.user})

@login_required
def building_search(request):
    form = BuildingSearchForm(request.GET)
    buildings = Building.objects.all()
    if form.is_valid():
        search = form.cleaned_data.get('search') # поиск
        buildings = buildings.filter(
            Q(ak__icontains=search) |
            Q(building_name__icontains=search) |
            Q(address__icontains=search)
        )
    return render(request, 'todos/building_search.html', {'form': form, 'buildings': buildings})

@login_required
def commentary_create(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.task = task
            commentary.user = request.user
            commentary.save()
            return redirect('task_list')
    else:
        form = CommentaryForm()
    return render(request, 'todos/commentary_form.html', {'form': form, 'task': task})

@login_required
@permission_required('todos.change_commentary', raise_exception=True)
def commentary_update(request, pk):
    commentary = get_object_or_404(Commentary, pk=pk)
    if request.method == 'POST':
        form = CommentaryForm(request.POST, instance=commentary)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = CommentaryForm(instance=commentary)
    return render(request, 'todos/commentary_form.html', {'form': form, 'commentary': commentary})

@login_required
@permission_required('todos.delete_commentary', raise_exception=True)
def commentary_delete(request, pk):
    commentary = get_object_or_404(Commentary, pk=pk)
    if request.method == 'POST':
        commentary.delete()
        return redirect('task_list')
    return render(request, 'todos/commentary_confirm_delete.html', {'commentary': commentary})
