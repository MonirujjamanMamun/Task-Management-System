from django.shortcuts import render
from task.models import TaskMode


def home(request):
    task_data = TaskMode.objects.all()
    return render(request, 'home.html', {'taskData': task_data})
