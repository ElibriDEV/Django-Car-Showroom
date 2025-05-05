from django.contrib.auth.models import User
from django.db import models as m
from phonenumber_field.modelfields import PhoneNumberField
from positions import PositionField

from utils.mixin import TimeStampMixin, LoggerMixin


class BannerModel(TimeStampMixin, LoggerMixin):
    title = m.CharField(max_length=255, verbose_name="Название баннера.")
    redirect_url = m.URLField(blank=True, null=True, default=None, verbose_name="Переход по клику.")
    image = m.ImageField(upload_to="static/banners", verbose_name="Изображение баннера.")
    position = PositionField(verbose_name="Позиция баннера.")

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class FeedBackRequestModel(TimeStampMixin, LoggerMixin):
    name = m.CharField(max_length=256, verbose_name="Имя.")
    phone = PhoneNumberField(region="RU")

    def __str__(self) -> str:
        return f"{self.phone} ({self.name})"

    class Meta:
        verbose_name = "Заказ звонка"
        verbose_name_plural = "Заказы звонков"
