from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('update/', ProfileUpdateView.as_view(), name='profile_update'),
]

app_name = "profiles"