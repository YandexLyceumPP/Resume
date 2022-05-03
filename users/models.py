from django.db import models
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField

User = get_user_model()


class Skills(models.Model):
    icon = models.ImageField('Иконка', upload_to='uploads/icons/', null=True)
    skill = models.CharField('Название', max_length=30)
    text = HTMLField('Описание')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.skill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/avatars/', null=True)
    skills = models.ManyToManyField(Skills, verbose_name='Skills', related_name='profile')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
