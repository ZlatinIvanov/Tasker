from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from tasker.accounts.forms import TaskerUserCreationForm, TaskerEditUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = TaskerUserCreationForm
    form = TaskerEditUserForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )