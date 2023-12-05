from typing import Any

from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models, transaction
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'
    
    def get_queryset(self, **kwargs: dict[str, Any]) -> QuerySet[Any]:
        return self.model.objects.all().select_related('user')

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль пользователя: {self.object.user.username}'
        return context
    

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    success_message = 'Профиль успешно обновлен!'
    template_name = 'profiles/profile_update.html'

    def get_object(self, queryset=None) -> Any:
        return self.request.user.profile

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form) -> HttpResponse:
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self) -> Any:
        return reverse_lazy('profile:profile_detail', kwargs={'pk': self.object.pk})