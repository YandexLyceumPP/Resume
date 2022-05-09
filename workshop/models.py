from django.db import models
from django.contrib.auth import get_user_model

from sorl.thumbnail import get_thumbnail

from tinymce.models import HTMLField
from core.models import ShowBaseModel

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


class Resume(ShowBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/avatars/", null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    text = HTMLField("Текст")
    date_edit = models.DateField()

    class Meta:
        verbose_name = verbose_name_plural = "Резюме"


# class Publication(ShowBaseModel):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
#     text = HTMLField("Текст")
#     date_edit = models.DateField("Дата редактирования", auto_now_add=True)

#     class Meta:
#         verbose_name = "Публикация"
#         verbose_name_plural = "Публикации"


# class File(ShowBaseModel):
#     publication = models.ForeignKey(
#         Publication, on_delete=models.CASCADE
#     )
#     file = models.FileField(upload_to="uploads/files/")

#     class Meta:
#         verbose_name = "Вложение"
#         verbose_name_plural = "Вложения"


# class Link(ShowBaseModel):
#     publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
#     icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
#     text = models.CharField("Текст", max_length=150)
#     url = models.URLField("URL")

#     class Meta:
#         verbose_name = "Ссылка"
#         verbose_name_plural = "Ссылки"

class Block(ShowBaseModel):
    title = models.CharField("Загаловок", max_length=200)
    order = models.IntegerField("Порядок")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class TextInfo(ShowBaseModel):
    text = HTMLField("Текст")
    order = models.IntegerField("Порядок")
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    decorate=models.TextField("Настройки отображения", blank=True)

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описания"

class FileInfo(ShowBaseModel):
    file = models.FileField(upload_to="uploads/files/")
    description = models.CharField("Подпись", max_length=200)
    order = models.IntegerField("Порядок")
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    decorate=models.TextField("Настройки отображения", blank=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class FileConfig(ShowBaseModel):
    text = HTMLField("Настройки")


    class Meta:
        verbose_name = "Файл настройки"
        verbose_name_plural = "Файлы настройки"