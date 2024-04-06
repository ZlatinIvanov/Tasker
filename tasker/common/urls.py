from django.urls import path

from tasker.common.views import IndexView, post_comment

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('tasks/task/<int:pk>/post-comment/', post_comment, name='post_comment'),

)