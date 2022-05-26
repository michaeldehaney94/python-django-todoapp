from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Class Based Generic Views
# listview is another way to get data and populate it in the index page
class TaskListView(ListView):
    model = Task
    template_name = 'todoapp/index.html'
    context_object_name = 'task_list'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todoapp/detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'todoapp/update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todoapp/delete.html'
    success_url = reverse_lazy('cbvindex')


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
