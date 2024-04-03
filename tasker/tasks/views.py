from django.contrib.auth import mixins as auth_mixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic as views

from tasker.common.forms import CommentForm, AttachmentForm
from tasker.tasks.models import Tasks
from tasker.tasks.forms import TaskCreateForm, TaskUpdateForm

SORT_OPTIONS = {
    'priority': 'priority',
    'created_at': 'created_at',
    'due_date': 'due_date',
    'title': 'title',
}


class ReadOnlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
        return form


class TaskCompletedListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Tasks
    template_name = 'tasks/completed_tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort')
        queryset = Tasks.objects.filter(state='Completed')
        if sort_by in SORT_OPTIONS:
            return queryset.order_by(SORT_OPTIONS[sort_by])
        return queryset


class TaskCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = TaskCreateForm
    template_name = 'tasks/task_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks_list')


class TaskDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Tasks
    template_name = "tasks/task_details.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['attachment_form'] = AttachmentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        comment_form = context['comment_form']
        attachment_form = context['attachment_form']

        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.task = self.object
                comment.user = request.user
                comment.save()
        elif 'attachment_submit' in request.POST:
            attachment_form = AttachmentForm(request.POST, request.FILES)
            if attachment_form.is_valid():
                attachment = attachment_form.save(commit=False)
                attachment.task = self.object
                attachment.user = request.user
                attachment.save()

        return self.render_to_response(context)


class TaskListView(views.ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Tasks.objects.filter(state='Not Done')
        sort_by = self.request.GET.get('sort')
        if sort_by in SORT_OPTIONS:
            return queryset.order_by(SORT_OPTIONS[sort_by])
        return queryset


class UserTasksListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Tasks
    template_name = 'tasks/user_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(assigned_to=self.request.user)


class TaskEditView(views.UpdateView):
    queryset = Tasks.objects.all()
    form_class = TaskUpdateForm
    template_name = "tasks/edit_task.html"

    def get_success_url(self):
        return reverse_lazy("task_details", kwargs={
            "pk": self.object.pk,
        })


class TaskCompleteView(views.UpdateView):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        return render(request, 'tasks/complete_task.html', {'task': task})

    def post(self, request, pk):
        # Process the completion of the task here
        task = get_object_or_404(Tasks, pk=pk)
        task.completed_at = timezone.now()
        task.state = 'Completed'
        task.save()
        return HttpResponseRedirect(reverse('tasks_list'))  # Redirect to task list after completion


class TaskDeleteView(views.DeleteView):
    queryset = Tasks.objects.all()
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks_list')

