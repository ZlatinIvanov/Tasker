from django import forms

from tasker.common.models import Comment, Attachment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file', 'description']