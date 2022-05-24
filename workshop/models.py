import os

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import date

from tinymce.models import HTMLField

from ordered_model.models import OrderedModel

from core.models import ShowBaseModel

from sorl.thumbnail import get_thumbnail

from workshop.validators import OrReValidator

User = get_user_model()


class DateEditBaseModel(models.Model):
    date_edit = models.DateField("Дата последнего редактирования", default=date.today)

    """def save(self, *args, **kwargs):
        self.date_edit = date.today
        # kwargs["commit"] = True
        super(DateEditBaseModel, self).save(*args, **kwargs)"""

    class Meta:
        abstract = True


class Icon(ShowBaseModel):
    image = models.ImageField("Иконка", upload_to="uploads/icons/", null=True)

    def get_image_100x100(self):
        return get_thumbnail(self.image, "100x100", quality=51)

    class Meta:
        verbose_name = "Иконка"
        verbose_name_plural = "Иконки"


class Tag(ShowBaseModel):
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


class Resume(ShowBaseModel, DateEditBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/avatars/", blank=True)
    contacts = models.ManyToManyField(Contact, verbose_name="Контакты", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", blank=True)
    text = HTMLField("Описание")

    def get_image_100x100(self):
        return get_thumbnail(self.image, "100x100", quality=51)

    class Meta:
        verbose_name = verbose_name_plural = "Резюме"


class Block(ShowBaseModel, OrderedModel, DateEditBaseModel):
    order_with_respect_to = "resume"

    title = models.CharField("Заголовок", max_length=200)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta(OrderedModel.Meta):
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

    def extension(self):
        # name, extension = os.path.splitext(self.file.name)
        ext = self.file.name.split('.')
        return "." + ext[-1]

    def name(self):
        name, extension = os.path.splitext(self.file.name)
        name = name.split("/")
        return name[-1]

    def is_image(self):
        ext = self.file.name.split('.')
        if ext[-1] in ["png", "jpg", "bmp", "jpeg"]:
            return True
        return False
    
    def is_file(self):
        return not self.is_image()

    def get_carousel_image(self):
        return get_thumbnail(self.file, "x300", quality=500)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
