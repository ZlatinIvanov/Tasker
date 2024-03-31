from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth.mixins import AccessMixin
from django.forms import DateInput
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views import generic as views

from tasker.accounts.forms import TaskerUserCreationForm
from tasker.accounts.models import Profile, TaskerUser


class OwnerRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class RegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = TaskerUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "accounts/details_profile.html"
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        filtered_queryset = queryset.filter(pk=pk)
        return filtered_queryset

    # def get_object(self, queryset=None):
    #     # Fetch the user's profile
    #     return get_object_or_404(Profile, user=self.request.user)


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    def get_success_url(self):
        return reverse_lazy("details profile", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["date_of_birth"].widget.attrs["type"] = "date"
        form.fields["date_of_birth"].label = "Birthday"
        return form


class ProfileDeleteView(views.DeleteView):
    queryset = TaskerUser.objects.all()
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy('index')
