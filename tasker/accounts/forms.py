from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.utils import timezone

from tasker.accounts.models import Profile

UserModel = get_user_model()


class TaskerUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class TaskerEditUserForm(auth_forms.UserChangeForm, forms.ModelForm):

    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel

