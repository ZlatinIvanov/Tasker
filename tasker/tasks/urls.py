from django.urls import path, include

from tasker.tasks.views import TaskCreateView, TaskDetailsView, TaskListView, TaskEditView, TaskDeleteView, \
    TaskCompleteView, TaskCompletedListView, UserTasksListView

urlpatterns = (
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('my_tasks/', UserTasksListView.as_view(), name='user_tasks'),
    path("completed/", TaskCompletedListView.as_view(), name="completed_tasks"),
    path(
        "task/<int:pk>/", include([
            path("", TaskDetailsView.as_view(), name="task_details"),
            path("edit/", TaskEditView.as_view(), name="edit_task"),
            path("delete/", TaskDeleteView.as_view(), name="delete_task"),
            path("complete/", TaskCompleteView.as_view(), name="complete_task"),

        ]),
         ),
)