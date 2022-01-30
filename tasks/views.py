# Add your Views Here

from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task



def all_tasks_view(request):
    pending_tasks = Task.objects.filter(completed=False).filter(deleted=False)
    completed_tasks = Task.objects.filter(completed=True).filter(deleted=False)
    return render(request, "all_tasks.html", {"pending_tasks": pending_tasks, "completed_tasks": completed_tasks})

def add_tasks_view(request):
    task_value = request.GET.get("task")
    task_obj = Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect("/tasks")

def completed_tasks_view(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, "completed_tasks.html", {"tasks": completed_tasks})

def complete_task_view(request, task_id):
    Task.objects.filter(id=task_id, deleted=False).update(completed=True)
    return HttpResponseRedirect("/all_tasks")

def delete_task_view(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    return HttpResponseRedirect("/tasks")

def tasks_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.filter(deleted=False).filter(completed=False)
    if search_term:
        tasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks, "search_result": True})