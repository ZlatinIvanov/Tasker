# Generated by Django 5.0.3 on 2024-04-10 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name_plural': 'tasks'},
        ),
    ]
