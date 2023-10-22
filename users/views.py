from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')


class RegisterUserView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile')