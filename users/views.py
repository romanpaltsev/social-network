from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from typing import Any

from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/form_view.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        context['btn_text'] = "Войти"
        return context


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/form_view.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        context['btn_text'] = "Зарегистрироваться"
        return context
    
    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user, backend='users.backends.EmailBackend')
        return super().form_valid(form)