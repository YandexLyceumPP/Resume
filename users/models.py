from django.contrib.auth import get_user_model
from django.db import models

from tinymce.models import HTMLField

from core.models import ShowBaseModel

from workshop.models import Icon

User = get_user_model()


class Skill(ShowBaseModel):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    skill = models.CharField("Название", max_length=30)
    text = HTMLField("Описание")

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/avatars/", null=True)
    skills = models.ManyToManyField(Skill)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Field(ShowBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=300)
    value = HTMLField("Значение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"
    