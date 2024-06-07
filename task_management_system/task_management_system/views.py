from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task

def home(request):
    task = Task.objects.all()
    return render(request, "home.html", {"data": task})