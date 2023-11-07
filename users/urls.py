from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import LoginUserView, RegisterUserView


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
]

app_name = "users"