from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from tasker.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if not created:
        return

    Profile.objects.create(user=instance)

    workers_group, _ = Group.objects.get_or_create(name='Workers')
    instance.groups.add(workers_group)
    instance.save()
