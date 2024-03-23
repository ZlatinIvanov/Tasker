from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views


class RegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    # form_class = RegisterForm
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


class DetailsProfileView(views.DetailView):
    pass


class EditProfileView(views.UpdateView):
    pass


class DeleteProfileView(views.DeleteView):
    pass
