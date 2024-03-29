from django.urls import path, include

from tasker.tasks.views import TaskCreateView, task_list, TaskDetailsView

urlpatterns = (
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('tasks_list/', task_list, name='tasks_list'),
    path(
        "task/<int:pk>/", include([
            path("", TaskDetailsView.as_view(), name="task_details"),
        ]),
         ),
)