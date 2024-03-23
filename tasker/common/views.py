from django.shortcuts import render
from django.views import generic as views

from tasker.tasks.models import Tasks


class IndexView(views.ListView):
    queryset = Tasks.objects.all() #.prefetch_related("pets").prefetch_related("photolike_set")

    template_name = "common/index.html"

    paginate_by = 1

    # @property
    # def pet_name_pattern(self):
    #     return self.request.GET.get("pet_name_pattern", None)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["pet_name_pattern"] = self.pet_name_pattern or ""
    #     return context
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     queryset = self.filter_by_pet_name_pattern(queryset)
    #
    #     return queryset
    #
    # def filter_by_pet_name_pattern(self, queryset):
    #     pet_name_pattern = self.pet_name_pattern
    #
    #     filter_query = {}
    #
    #     if pet_name_pattern:
    #         filter_query['pets__name__icontains'] = pet_name_pattern
    #
    #     return queryset.filter(**filter_query)

