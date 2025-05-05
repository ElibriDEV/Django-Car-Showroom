from django.contrib.auth.models import User
from django.db import models as m
from django.urls import reverse

from utils.mixin import TimeStampMixin, LoggerMixin


class PostModel(TimeStampMixin, LoggerMixin):
    title = m.CharField(max_length=256, verbose_name="Заголовок")
    content = m.TextField(verbose_name="Содержание")
    preview_content = m.CharField(max_length=256, verbose_name="Краткое содержание", null=True, blank=True)
    image = m.ImageField(upload_to="static/images/posts", verbose_name="Изображение")
    author = m.ForeignKey(User, on_delete=m.CASCADE, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("posts:post-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class CommentModel(TimeStampMixin, LoggerMixin):
    post = m.ForeignKey(PostModel, on_delete=m.CASCADE, verbose_name="Блог")
    text = m.TextField(verbose_name="Текст комментария")
    author = m.ForeignKey(User, on_delete=m.CASCADE, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
