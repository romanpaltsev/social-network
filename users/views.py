from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/form_view.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        context['btn_text'] = "Войти"
        return context


class RegisterUserView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'users/form_view.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        context['btn_text'] = "Зарегистрироваться"
        return context
