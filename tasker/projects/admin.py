from django.contrib import admin

from tasker.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'clients', 'description', 'date_created')
    list_filter = ('name', 'clients', 'description', 'date_created')
    search_fields = ('name', 'client', 'date_created')
