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


class TaskDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    queryset = Tasks.objects.all()
    template_name = "tasks/task_details.html"
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        filtered_queryset = queryset.filter(pk=pk)
        return filtered_queryset


class TaskListView(views.ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort')
        if sort_by == 'priority':
            return Tasks.objects.order_by('priority')
        elif sort_by == 'created_at':
            return Tasks.objects.order_by('created_at')
        elif sort_by == 'due_date':
            return Tasks.objects.order_by('due_date')
        elif sort_by == 'title':
            return Tasks.objects.order_by('title')
        else:
            return Tasks.objects.all()
