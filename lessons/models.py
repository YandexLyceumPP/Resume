from django.db import models

from core.models import ShowBaseModel


class Topic(ShowBaseModel):
    title = models.CharField('Название', max_length=150)
    text = models.TextField('Описание')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title


class Lesson(ShowBaseModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic')
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title
