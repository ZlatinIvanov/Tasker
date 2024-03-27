from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


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


class TaskState(models.Model):
    pass



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
        help_text="Enter the task due date",
        verbose_name="Task due date",
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        help_text="Enter the task priority",
        verbose_name="Task priority",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Enter the task creation date",
        verbose_name="Task creation date",
    )
    #
    # updated_at = models.DateTimeField(
    #     auto_now=True,
    # )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        help_text="Enter the task difficulty",
        verbose_name="Task difficulty",
    )

    assigned_to = models.ForeignKey(
        UserModel,
        related_name='assigned_tasks',
        on_delete=models.DO_NOTHING,
        help_text="Enter the task assigned to",
        verbose_name="Task assigned to",

    )

    def __str__(self):
        return self.title
