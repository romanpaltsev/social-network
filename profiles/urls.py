from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProfileUserView


urlpatterns = [
    path('<int:pk>/', ProfileUserView.as_view(), name='profile'),
]

app_name = "profiles"