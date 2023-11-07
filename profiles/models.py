from django.contrib.auth import get_user_model
from django.db import models
import uuid

from core.models import BaseModel


User = get_user_model()

def rename_image(instance, filename) -> str:
    image_name = str(uuid.uuid4())
    image_type = filename.split('.')[-1]
    return f'avatar/{image_name}.{image_type}'


class Profile(BaseModel):
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = [
        ("MALE", "Мужчина"),
        ("FEMALE", "Женщина"),
    ]

    user = models.OneToOneField(
        verbose_name="Пользователь",
        to=User,
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(
        verbose_name="Аватарка",
        default='/static/avatar/avatar.jpg',
        upload_to=rename_image,
        null=True,
        blank=True,
        help_text="Изображение пользователя",
    )
    birthday = models.DateField(
        verbose_name="День рождения",
        null=True,
        blank=True,
    )
    bio = models.CharField(
        verbose_name="О себе",
        max_length=1024,
        null=True,
        blank=True,
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name="Пол",
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        help_text="Пол пользователя",
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=50,
        null=True,
        blank=True,
    )
    telegram = models.CharField(
        verbose_name="Телеграм",
        max_length=50,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.user.username)