from django.contrib.auth import get_user_model
from django.db import models

from tinymce.models import HTMLField
from workshop.models import Icon
from core.models import ShowBaseModel

User = get_user_model()


class Skill(ShowBaseModel):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    skill = models.CharField("Название", max_length=30)
    text = HTMLField("Описание")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.skill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/avatars/", null=True)
    skills = models.ManyToManyField(Skill, verbose_name="Skill")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Field(ShowBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField("Иконка", upload_to="uploads/icons/", null=True)
    title = models.CharField("Навазние", max_length=20)
    value = models.CharField("Значение", max_length=100)

    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"


class Block(ShowBaseModel):
    title = models.CharField("Загаловок", max_length=200)
    