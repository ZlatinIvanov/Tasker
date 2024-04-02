from django import forms

from tasker.tasks.models import Tasks


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority', 'difficulty', 'assigned_to', 'project', 'due_date', ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority', 'difficulty','assigned_to', 'project', 'due_date', ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
