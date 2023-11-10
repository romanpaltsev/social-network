from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=100,
        unique=True,
        help_text="Электронная почта должна быть уникальной",
    )

    def __str__(self):
        return self.email
