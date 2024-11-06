from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Привет, мир!")

def task_by_id(request, task_id):
    if task_id > 10:
        return HttpResponse("Такой задачи нет", status=404)
    return HttpResponse(f"Вы открыли задачу {task_id}")

def get_all_tasks(request):
    return HttpResponse("Все задачи")