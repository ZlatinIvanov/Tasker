# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
#
# from tasker.accounts.models import TaskerUser
# from tasker.tasks.models import Tasks
#
# directors_group, _ = Group.objects.get_or_create(name='Directors')
# managers_group, _ = Group.objects.get_or_create(name='Managers')
# workers_group, _ = Group.objects.get_or_create(name='Workers')
#
# content_type = ContentType.objects.get_for_model(TaskerUser)
# permission = Permission.objects.get(codename='change_user')
# directors_group.permissions.add(permission)

# task_content_type = ContentType.objects.get_for_model(Tasks)
# view_permission = Permission.objects.get(codename='task_content')
# add_permission = Permission.objects.get(codename='add_task')
# change_permission = Permission.objects.get(codename='change_task')
# delete_permission = Permission.objects.get(codename='delete_task')


# class CustomGroups(models.Model):
#     django_group = models.OneToOneField(
#         Group,
#         on_delete=models.CASCADE,
#     )
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     def __str__(self):
#         return self.django_group.name
