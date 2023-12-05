from typing import Any

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/form_view.html'
    redirect_authenticated_user = True
    success_message = 'Вы успешно вошли в личный кабинет!'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        context['btn_text'] = "Войти"
        return context


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/form_view.html'
    success_message = 'Вы успешно зарегистрировались!'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        context['btn_text'] = "Зарегистрироваться"
        return context