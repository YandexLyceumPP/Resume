from django.db import models
from django.contrib.auth import get_user_model
from ordered_model.models import OrderedModel

from tinymce.models import HTMLField
from core.models import ShowBaseModel
from workshop.validators import OrReValidator

User = get_user_model()


class Tag(ShowBaseModel):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(
        "Номер телефона | Email | URL",
        max_length=1000,
        validators=[
            OrReValidator(
                (
                    r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.[a-z0-9]+",
                    r"\+?1?\d{8,15}",
                    r"https?://[a-zA-Z0-1]+.[a-zA-Z0-1]+(/[a-zA-Z0-1]+)*/?"
                )
            )
        ]
    )

    def __str__(self):
        return self.contact

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Resume(ShowBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/avatars/", null=True)
    contacts = models.ManyToManyField(Contact, verbose_name="Контакты")
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    text = HTMLField("Описание")
    date_edit = models.DateField()

    def __str__(self):
        return f"[{self.date_edit}] {self.text[:20]}"

    class Meta:
        verbose_name = verbose_name_plural = "Резюме"


class Block(ShowBaseModel, OrderedModel):
    title = models.CharField("Загаловок", max_length=200)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"


class Text(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    text = HTMLField("Текст")

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Текста"


class File(ShowBaseModel):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/files/")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
