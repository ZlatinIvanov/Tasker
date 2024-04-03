# from django.db import models
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission
# from django.contrib.auth.decorators import permission_required
# from django.contrib.auth.mixins import PermissionRequiredMixin
#
# from tasker.tasks.models import Tasks, TaskState
#
# directors_group, _ = Group.objects.get_or_create(name='Directors')
# managers_group, _ = Group.objects.get_or_create(name='Managers')
# workers_group, _ = Group.objects.get_or_create(name='Workers')
#
#
# directors_group.permissions.add(Permission.objects.get(codename='add_profile'))
# directors_group.permissions.add(Permission.objects.get(codename='change_profile'))
# directors_group.permissions.add(Permission.objects.get(codename='delete_profile'))
# directors_group.permissions.add(Permission.objects.get(codename='view_profile'))
# directors_group.permissions.add(Permission.objects.get(codename='add_task'))
# directors_group.permissions.add(Permission.objects.get(codename='change_task'))
# directors_group.permissions.add(Permission.objects.get(codename='delete_task'))
# directors_group.permissions.add(Permission.objects.get(codename='view_task'))
#
# managers_group.permissions.add(Permission.objects.get(codename='add_task'))
# managers_group.permissions.add(Permission.objects.get(codename='change_task'))
# managers_group.permissions.add(Permission.objects.get(codename='delete_task'))
# managers_group.permissions.add(Permission.objects.get(codename='view_task'))
# managers_group.permissions.add(Permission.objects.get(codename='view_profile'))
#
# workers_group.permissions.add(Permission.objects.get(codename='view_profile'))
# workers_group.permissions.add(Permission.objects.get(codename='view_task'))
#
from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Comment(models.Model):
    task = models.ForeignKey(
        'tasks.Tasks',
        related_name="comments",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Attachment(models.Model):
    task = models.ForeignKey(
        'tasks.Tasks',
        related_name="attachments",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='attachments',
    )
    description = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )