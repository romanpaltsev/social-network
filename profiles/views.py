from django.views.generic import DetailView
from typing import Any

from .models import Profile


class ProfileUserView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль пользователя: {self.object.user.username}'
        return context