from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterUserForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = RegisterUserForm


admin.site.register(CustomUser, CustomUserAdmin)