from django.shortcuts import render
from django.views import generic as views

from tasker.tasks.models import Tasks


class HasPermissionMixin:
    permission_classes = []


class IndexView(views.ListView):
    queryset = Tasks.objects.all()

    template_name = "common/index.html"

    paginate_by = 1



