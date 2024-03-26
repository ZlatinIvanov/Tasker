from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from tasker.tasks.models import Tasks

from tasker.tasks.forms import TaskCreateForm


def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})


class TaskCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'
    queryset = Tasks.objects.all()

    def get_success_url(self):
        return reverse('tasks_list')


