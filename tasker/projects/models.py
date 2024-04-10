from django.db import models


class Project(models.Model):
    name = models.CharField(
        max_length=50,
    )
    clients = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        default=None,
        blank=True,
        null=True,
    )
    date_created = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name