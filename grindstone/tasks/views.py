from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TaskForm
from .models import Task


class TaskList(ListView):
    model = Task
    paginate_by = 20


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')


class TaskDetail(DetailView):
    model = Task


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
