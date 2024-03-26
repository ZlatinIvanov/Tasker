from django import forms

from tasker.tasks.models import Tasks


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority', 'difficulty', 'due_date', 'assigned_to',]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }