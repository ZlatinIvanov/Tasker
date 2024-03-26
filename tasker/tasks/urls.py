from django.urls import path

from tasker.tasks.views import TaskCreateView, task_list

urlpatterns = (
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('tasks_list/', task_list, name='tasks_list'),
)