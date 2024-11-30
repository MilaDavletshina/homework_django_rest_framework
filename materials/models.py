from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название курса", help_text="Укажите курс"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )
    image = models.ImageField(
        upload_to="materials/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название урока", help_text="Укажите урок"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    video_link = models.URLField(max_length=200, blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="курс"
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
