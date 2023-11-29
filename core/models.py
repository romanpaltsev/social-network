from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name="Активность",
        default=True,
    )