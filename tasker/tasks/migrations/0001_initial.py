# Generated by Django 5.0.3 on 2024-03-24 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the task title', max_length=50, verbose_name='Task title')),
                ('description', models.TextField(help_text='Enter the task description', max_length=500, verbose_name='Task description')),
                ('due_date', models.DateField(help_text='Enter the task due date', verbose_name='Task due date')),
                ('priority', models.CharField(choices=[('LOW', 'LOW'), ('NORMAL', 'NORMAL'), ('HIGH', 'HIGH')], help_text='Enter the task priority', max_length=20, verbose_name='Task priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Enter the task creation date', verbose_name='Task creation date')),
                ('difficulty', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], help_text='Enter the task difficulty', max_length=20, verbose_name='Task difficulty')),
                ('assigned_to', models.ForeignKey(help_text='Enter the task assigned to', on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Task assigned to')),
            ],
        ),
    ]