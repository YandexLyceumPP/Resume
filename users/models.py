from django.contrib.auth import get_user_model
from django.db import models
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField

from core.models import ShowBaseModel

User = get_user_model()


class Skill(ShowBaseModel):
    skill = models.CharField("Название", max_length=100)
    text = HTMLField("Описание", null=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/avatars/profile/", null=True)
    skills = models.ManyToManyField(Skill)

    def get_image(self):
        return get_thumbnail(self.image, "200x200", quality=51) if self.image else None

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Field(ShowBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=300)
    value = HTMLField("Значение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"
    