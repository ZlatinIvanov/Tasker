from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from tasker.accounts.models import TaskerUser

UserModel = get_user_model()

DIFFICULTY_CHOICES = (
    ('EASY', 'EASY'),
    ('MEDIUM', 'MEDIUM'),
    ('HARD','HARD'),
)

PRIORITY_CHOICES = (
    ('LOW', 'LOW'),
    ('NORMAL', 'NORMAL'),
    ('HIGH', 'HIGH'),
)


class TaskState(models.TextChoices):
    COMPLETE = "Completed"
    NOT_DONE = "Not Done"


class Tasks(models.Model):

    title = models.CharField(
        max_length=50,
        help_text="Enter the task title",
        verbose_name="Task title",
    )

    description = models.TextField(
        max_length=500,
        help_text="Enter the task description",
        verbose_name="Task description",
    )

    due_date = models.DateField(
        help_text="Choose the task due date",
        verbose_name="Task due date",
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        help_text="Choose the task priority",
        verbose_name="Task priority",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Task creation date",
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        help_text="Choose the task difficulty",
        verbose_name="Task difficulty",
    )
    state = models.CharField(
        max_length=20,
        choices=TaskState.choices,
        default=TaskState.NOT_DONE,
        verbose_name="Task state",
    )

    assigned_to = models.ForeignKey(
        UserModel,
        related_name='assigned_tasks',
        on_delete=models.DO_NOTHING,
        help_text="Choose the task assigned to",
        verbose_name="Task assigned to",
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        TaskerUser,
        related_name='creator',
        on_delete=models.DO_NOTHING,
        help_text="Choose the task created by",
        verbose_name="Task created by",
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Task completion date",
    )

    def mark_as_done(self):
        self.state = TaskState.COMPLETE
        self.save()

    def __str__(self):
        return self.title
