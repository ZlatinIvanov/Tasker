from django.contrib import admin

from tasker.tasks.models import Tasks


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'due_date', 'priority', 'difficulty', 'assigned_to_email')

    def assigned_to_email(self, obj):
        return ', '.join([user.email for user in obj.assigned_to.all()])

    assigned_to_email.short_description = 'Assigned To'
