from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db.models import Prefetch
from django.forms import DateInput
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from django.views import generic as views

from tasker.accounts.forms import TaskerUserCreationForm
from tasker.accounts.models import Profile, TaskerUser
from tasker.common.templatetags.paging import get_paginated_context_data

SORT_OPTIONS = {
    'email': 'email',
    'name': 'name',
    'date_joined': 'date_joined',
}


def is_director(user):
    return user.groups.filter(name='Directors').exists()


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = self.get_object()
        context['profile_picture'] = profile.profile_picture
        context['can_edit_or_delete'] = self.can_edit_or_delete(user, profile)
        return context

    def can_edit_or_delete(self, user, profile):
        # Check if the user is in the Directors group or is the owner of the profile
        return user.groups.filter(name='Directors').exists() or user == profile.user


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user or self.request.user.groups.filter(name='Directors').exists()

    def get_success_url(self):
        return reverse_lazy("details profile", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        user_in_directors_group = self.request.user.groups.filter(name='Directors').exists()
        context['can_edit_or_delete'] = user_in_directors_group or profile.user == self.request.user
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["date_of_birth"].widget.attrs["type"] = "date"
        form.fields["date_of_birth"].label = "Birthday"
        return form

    def form_valid(self, form):
        print("Inside form_valid method")

        response = super().form_valid(form)

        # Handle profile picture
        profile_picture = form.cleaned_data.get("profile_picture")
        if profile_picture:

            self.object.profile_picture = profile_picture
            self.object.save()

        # Handle group change
        if 'groups' in form.cleaned_data:
            group_name = form.cleaned_data['groups']
            if self.request.user.groups.filter(name='Directors').exists():

                user = self.object.user
                group = Group.objects.get(name=group_name)
                user.groups.clear()
                user.groups.add(group)
                print("User group updated:", user.groups.all())
            else:
                print("User is not in Directors group")
        return response


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    model = TaskerUser
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.comment_set.all().delete()

        self.object.attachment_set.all().delete()

        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())


class ProfileListView(LoginRequiredMixin, views.ListView):
    queryset = TaskerUser.objects.all()
    template_name = "accounts/profile_list.html"
    context_object_name = 'profile_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = TaskerUser.objects.all()
        sort_by = self.request.GET.get('sort')
        full_name_filter = self.request.GET.get('full_name')
        email_filter = self.request.GET.get('email')

        if sort_by in SORT_OPTIONS:
            return queryset.order_by(SORT_OPTIONS[sort_by])
        if full_name_filter:
            profiles = Profile.objects.filter(first_name__icontains=full_name_filter) | Profile.objects.filter(
                last_name__icontains=full_name_filter)
            queryset = TaskerUser.objects.filter(profile__in=profiles)
        if email_filter:
            queryset = queryset.filter(email__icontains=email_filter)
        return queryset
