import datetime as dt

from django.core.validators import MinValueValidator
from django.db import models as m
from django.urls import reverse
from django_countries.fields import CountryField
from positions import PositionField

from utils.mixin import TimeStampMixin, LoggerMixin


class BrandModel(TimeStampMixin, LoggerMixin):
    name = m.CharField(max_length=256, unique=True, verbose_name="Название Производителя.")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class ModelModel(TimeStampMixin, LoggerMixin):
    name = m.CharField(max_length=256, unique=True, verbose_name="Название модели.")
    brand = m.ForeignKey(to=BrandModel, on_delete=m.CASCADE, verbose_name="Производитель.")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


def _year_choices() -> list[tuple[int, int]]:
    return [(r, r) for r in range(1984, dt.date.today().year + 1)]


class AutomobileModel(TimeStampMixin, LoggerMixin):
    DRIVE_CHOICES = [
        ("FWD", "Передний Привод"),
        ("AWD", "Полный Привод"),
        ("RWD", "Задний Привод"),
    ]
    CATEGORY_CHOICES = [
        ("AUTO", "Автомобиль"),
        ("TRUCK", "Грузовик"),
    ]
    BODY_CHOICES = [
        ("SEDAN", "Седан"),
        ("COUPE", "Купе"),
        ("HATCHBACK", "Хетчбэк"),
        ("LIFTBACK", "Лифтбэк"),
        ("FASTBACK", "Фастбэк"),
        ("UNIVERSAL", "Универсал"),
        ("CROSSOVER", "Кроссовер"),
        ("OFFROAD", "Внедорожник"),
        ("PICKUP", "Пикап"),
        ("LIGHTVAN", "Легковой фургон"),
        ("MINIVAN", "Минивен"),
        ("COMPACTVAN", "Компактвен"),
        ("MICROVAN", "Микровен"),
        ("CABRIO", "Кабриолет"),
        ("ROADSTER", "Родстер"),
        ("TARGA", "Тарга"),
        ("LANDO", "Ландо"),
        ("LIMOUSINE", "Лимузин"),
        ("TRUCK", "Тягач"),
    ]
    description = m.TextField(null=True, blank=True, default=None, verbose_name="Описание товара.")

    brand = m.ForeignKey(to=BrandModel, on_delete=m.RESTRICT, verbose_name="Производитель.")
    model = m.ForeignKey(to=ModelModel, on_delete=m.RESTRICT, verbose_name="Модель.")

    category = m.CharField(choices=CATEGORY_CHOICES, max_length=256, verbose_name="Категория.")
    year = m.IntegerField(choices=_year_choices(), verbose_name="Год выпуска.")
    mileage = m.IntegerField(validators=[MinValueValidator(0)], verbose_name="Пробег.")
    used = m.BooleanField(verbose_name="БУ.")
    color = m.CharField(max_length=256, verbose_name="Цвет.")
    power = m.IntegerField(validators=[MinValueValidator(0)], verbose_name="Мощность.")
    drive = m.CharField(max_length=3, choices=DRIVE_CHOICES, verbose_name="Привод.")
    body = m.CharField(max_length=128, choices=BODY_CHOICES, verbose_name="Кузов.")
    country = CountryField(verbose_name="Страна.")
    price = m.DecimalField(max_digits=16, decimal_places=2, verbose_name="Цена.")
    sold = m.BooleanField(default=False, verbose_name="Продано.")
    reserved = m.BooleanField(default=False, verbose_name="Зарезервировано.")

    def __str__(self) -> str:
        return f"{self.brand} {self.model}, {self.year}, {self.mileage} км."

    def get_absolute_url(self):
        return reverse("catalog:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class AutomobileImage(TimeStampMixin, LoggerMixin):
    image = m.ImageField(upload_to ="static/images/auto", verbose_name="Изображение.")
    position = PositionField(collection="automobile", verbose_name="Позиция.")
    automobile = m.ForeignKey(to=AutomobileModel, on_delete=m.CASCADE, verbose_name="Автомобиль.", related_name="images")

    def __str__(self) -> str:
        return str(self.image)

    class Meta:
        verbose_name = "Изображение автомобиля"
        verbose_name_plural = "Изображения автомобиля"
