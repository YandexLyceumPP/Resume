from django.db import models
from django.contrib.auth import get_user_model
from ordered_model.models import OrderedModel

from sorl.thumbnail import get_thumbnail

from tinymce.models import HTMLField
from core.models import ShowBaseModel
from workshop.validators import OrReValidator

User = get_user_model()


class Icon(ShowBaseModel):
    image = models.ImageField("Иконка", upload_to="uploads/icons/", null=True)

    def get_image_100x100(self):
        return get_thumbnail(self.image, "100x100", quality=51)

    class Meta:
        verbose_name = "Иконка"
        verbose_name_plural = "Иконки"


class Tag(ShowBaseModel):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=100)

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

    class Meta:
        verbose_name = verbose_name_plural = "Резюме"


class Block(ShowBaseModel, OrderedModel):
    title = models.CharField("Загаловок", max_length=200)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

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
    file = models.FileField(upload_to="uploads/files/")
    description = models.CharField("Подпись", max_length=200)
    order = models.IntegerField("Порядок")
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    decorate = models.TextField("Настройки отображения", blank=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class FileConfig(ShowBaseModel):
    text = HTMLField("Настройки")

    class Meta:
        verbose_name = "Файл настройки"
        verbose_name_plural = "Файлы настройки"