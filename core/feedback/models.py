from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as m

from utils.mixin import TimeStampMixin, LoggerMixin


class FeedbackModel(TimeStampMixin, LoggerMixin):
    username = m.CharField(max_length=256, verbose_name="Имя пользователя")
    email = m.EmailField(verbose_name="Email пользователя")
    usability = m.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Оценка удобства сайта")
    design = m.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Оценка дизайна сайта")
    wishes = m.TextField(null=True, blank=True, verbose_name="Пожелания к сайту")
    newsletter = m.BooleanField(verbose_name="Подписка на рассылку", null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
