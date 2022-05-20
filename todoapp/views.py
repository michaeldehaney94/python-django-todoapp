from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Task


# Create your views here.
def index(request):
    task_list = Task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'todoapp/index.html', {'task_list': task_list})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'todoapp/delete.html', {'task': task})


def edit(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'todoapp/edit.html', {'task': task, 'form': form})
