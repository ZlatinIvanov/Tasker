from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


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