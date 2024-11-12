from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Task, Building, Commentary
from .forms import TaskForm, BuildingForm, BuildingSearchForm, CommentaryForm

@login_required
def task_list(request):
    tasks = Task.objects.all()
    users_count = User.objects.count()

    # Добавляем пагинацию
    paginator = Paginator(tasks, 10)  # Показывать 10 задач на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todos/task_list.html', {'page_obj': page_obj, 'users_count': users_count})

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
    buildings = Building.objects.all()

    # Добавляем пагинацию
    paginator = Paginator(buildings, 10)  # Показывать 10 зданий на странице
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def about(request):
    return render(request, 'todos/about.html')

@login_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'todos/users_list.html', {'users': users})

@login_required
def personal_account(request):
    return render(request, 'todos/personal_account.html', {'user': request.user})

@login_required
def building_search(request):
    form = BuildingSearchForm(request.GET)
    buildings = Building.objects.all()
    if form.is_valid():
        search = form.cleaned_data.get('search')
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
        form = CommentaryForm(initial={'text': 'Выполнено'})
    return render(request, 'todos/commentary_form.html', {'form': form})

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
    return render(request, 'todos/commentary_form.html', {'form': form})

@login_required
@permission_required('todos.delete_commentary', raise_exception=True)
def commentary_delete(request, pk):
    commentary = get_object_or_404(Commentary, pk=pk)
    if request.method == 'POST':
        commentary.delete()
        return redirect('task_list')
    return render(request, 'todos/commentary_confirm_delete.html', {'commentary': commentary})
