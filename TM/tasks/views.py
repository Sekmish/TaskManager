from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': None, 'create': True})

def task_delete(request, id):
    task = Task.objects.get(id=id)
    completed = task.completed
    task.delete()
    if completed:
        return redirect('completed_task_list')
    else:
        return redirect('task_list')

def task_edit(request, id):
    task = Task.objects.get(id=id)
    completed = task.completed
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        if 'completed' in request.POST:
            task.completed = True
            task.save()
        if completed:
            return redirect('completed_task_list')
        else:
            return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task, 'create': False, 'completed': completed})

def completed_task_list(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/completed_task_list.html', {'tasks': tasks})

def task_return(request, id):
    task = Task.objects.get(id=id)
    task.completed = False
    task.save()
    return redirect('completed_task_list')