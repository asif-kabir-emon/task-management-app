from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')

def complete_task(request, id):
    task = Task.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')