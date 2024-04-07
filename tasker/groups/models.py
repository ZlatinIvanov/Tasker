from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

from tasker.tasks.models import Tasks


def create_groups_with_permissions():
    # Create groups
    directors_group, _ = Group.objects.get_or_create(name='Directors')
    managers_group, _ = Group.objects.get_or_create(name='Managers')
    workers_group, _ = Group.objects.get_or_create(name='Workers')

    # Define permissions
    task_content_type = ContentType.objects.get_for_model(Tasks)  # Assuming Task is your model
    view_permission = Permission.objects.get(codename='task_content')
    add_permission = Permission.objects.get(codename='add_task')
    change_permission = Permission.objects.get(codename='change_task')
    delete_permission = Permission.objects.get(codename='delete_task')

    # Assign permissions to groups
    directors_group.permissions.add(view_permission, add_permission, change_permission, delete_permission)
    managers_group.permissions.add(view_permission, add_permission, change_permission)
    workers_group.permissions.add(view_permission)

    # Optionally, add users to groups
    # user = User.objects.get(username='example_user')
    # directors_group.user_set.add(user)
    # managers_group.user_set.add(user)
    # workers_group.user_set.add(user)


class CustomGroups(models.Model):
    django_group = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.django_group.name
