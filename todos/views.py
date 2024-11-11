from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Task, Building
from .forms import TaskForm, BuildingForm

@login_required
def task_list(request):
    tasks = Task.objects.all()
    users_count = User.objects.count()
    return render(request, 'todos/task_list.html', {'tasks': tasks, 'users_count': users_count})

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
    return render(request, 'todos/building_list.html', {'buildings': buildings})

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
