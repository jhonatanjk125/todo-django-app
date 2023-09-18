from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markComplete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')


def markUndone(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        new_task = request.POST['new_task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task':task
        }
        return render(request, 'edit_task.html', context)


def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('home')
