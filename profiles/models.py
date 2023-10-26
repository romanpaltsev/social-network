from django.contrib.auth import get_user_model
from django.db import models
import uuid


User = get_user_model()


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = [
        ("MALE", "Мужчина"),
        ("FEMALE", "Женщина"),
    ]

    user = models.OneToOneField(
        name="Пользователь",
        to=User,
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(
        name="Аватарка"
        default='avatar/avatar.jpg',
        upload_to=rename_image,
        null=True,
        blank=True,
        help_text="Изображение пользователя",
    )
    birthday = models.DateField(
        name="День рождения",
        null=True,
        blank=True,
    )
    bio = models.CharField(
        name="О себе",
        max_length=1024,
        null=True,
        blank=True,
    )
    gender = models.PositiveSmallIntegerField(
        name="Пол",
        max_length=2,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        help_text="Пол пользователя",
    )
    city = models.CharField(
        name="Город",
        max_length=50,
        null=True,
        blank=True,
    )
    telegram = models.CharField(
        name="Телеграм",
        max_length=50,
        null=True,
        blank=True,
    )

    def rename_image(instance, filename):
        image_name = str(uuid.uuid4())
        image_type = filename.split('.')[-1]
        return f'avatar/{image_name}.{image_type}'

    def __str__(self):
        return str(self.user.username)