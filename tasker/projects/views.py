from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from tasker.common.templatetags.paging import get_paginated_context_data
from tasker.projects.forms import ProjectCreateForm, ProjectUpdateForm
from tasker.projects.models import Project

SORT_OPTIONS = {
    'name': 'name',
    'clients': 'clients',
    'date_created': 'date_created',
}


class ProjectCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = ProjectCreateForm
    template_name = 'projects/create_project.html'
    success_url = reverse_lazy('projects_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Project
    template_name = "projects/project_details.html"
    pk_url_kwarg = 'pk'


class ProjectListView(views.ListView):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        page_number = self.request.GET.get('page')
        context.update(get_paginated_context_data(queryset, self.paginate_by, page_number))
        return context

    def get_queryset(self):
        queryset = Project.objects.all()
        sort_by = self.request.GET.get('sort')
        name_filter = self.request.GET.get('name')
        client_filter = self.request.GET.get('client')

        if sort_by in SORT_OPTIONS:
            return queryset.order_by(SORT_OPTIONS[sort_by])

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        if client_filter:
            queryset = queryset.filter(clients__icontains=client_filter)

        return queryset


class ProjectEditView(views.UpdateView):
    queryset = Project.objects.all()
    form_class = ProjectUpdateForm
    template_name = "projects/edit_project.html"

    def get_success_url(self):
        return reverse_lazy("project_details", kwargs={
            "pk": self.object.pk,
        })


class ProjectDeleteView(views.DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    success_url = reverse_lazy('projects_list')
