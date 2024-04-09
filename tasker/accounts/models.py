from django.contrib.auth.models import User, Group
from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from tasker.accounts.managers import TaskerUserManager


class TaskerUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = TaskerUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        default=None,
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        default=None,
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        default=None,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        default=None,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        TaskerUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name


# @receiver(post_save, sender=TaskerUser)
# def add_to_workers_group(sender, instance, created, **kwargs):
#     workers_group, _ = Group.objects.get_or_create(name='Workers')
#     if created:
#         instance.groups.add(workers_group)
#         instance.save()
