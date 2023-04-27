from django.contrib.auth.models import AbstractUser
from django.db import models


class Articles(models.Model):
    topic = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, verbose_name='Имя')
    rev = models.TextField(blank=True, verbose_name='Отзыв')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
