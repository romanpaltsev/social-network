from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from core.models import BaseModel


User = get_user_model()

class Post(BaseModel):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']
        

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
        null=False,
    )
    content = models.TextField(
        verbose_name="Описание",
        max_length=5000,
        null=False,
    )    
    author = models.ForeignKey(
        verbose_name="Автор",
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'pk': self.pk})