from django.shortcuts import render, redirect
from . forms import AddTaskForms
from task.models import TaskMode
# Create your views here.


def add_task(request):
    if request.method == "POST":
        task_form = AddTaskForms(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = AddTaskForms()
    return render(request, 'task.html', {'form': task_form})


def edit_task(request, id):
    task_data = TaskMode.objects.get(pk=id)
    task_form = AddTaskForms(instance=task_data)
    if request.method == "POST":
        task_form = AddTaskForms(request.POST, instance=task_data)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, 'task.html', {'form': task_form})


def delete_task(request, id):
    task_data = TaskMode.objects.get(pk=id)
    task_data.delete()
    return redirect('home')
