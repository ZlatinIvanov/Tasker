from django.urls import path, include

from tasker.projects.views import ProjectListView, ProjectDetailsView, ProjectEditView, ProjectDeleteView, \
    ProjectCreateView

urlpatterns = (
    path('create_project/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path(
        "project/<int:pk>/", include([
            path("", ProjectDetailsView.as_view(), name="project_details"),
            path("edit/", ProjectEditView.as_view(), name="edit_project"),
            path("delete/", ProjectDeleteView.as_view(), name="delete_project"),
        ]),
    ),
)