from django.shortcuts import get_object_or_404, redirect
from django.views import generic as views

from tasker.common.models import Comment
from tasker.tasks.models import Tasks


class HasPermissionMixin:
    permission_classes = []


class IndexView(views.ListView):
    queryset = Tasks.objects.all()

    template_name = "common/index.html"

    paginate_by = 1


def post_comment(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Tasks, pk=task_id)
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment.objects.create(task=task, user=request.user, comment=comment_text)
    return redirect('task_details', pk=task_id)

