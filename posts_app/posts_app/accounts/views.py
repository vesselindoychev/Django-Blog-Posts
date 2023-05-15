from django.contrib.auth import views as auth_views, login
from django.views import generic as views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from posts_app.accounts.forms import CreateProfileForm
from posts_app.accounts.models import Profile


class RegisterUserView(views.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterUserView, self).get(*args, **kwargs)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        next_page = self.request.GET.get('next', None)
        if next_page:
            return next_page
        return reverse_lazy('home')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(LoginUserView, self).get(*args, **kwargs)


class LogoutUserView(auth_views.LogoutView):
    pass
