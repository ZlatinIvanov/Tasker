from django.contrib import admin
from tasker.common.models import Comment, Attachment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'comment', 'created_at')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'file', 'description', 'created_at')
