from django.db import models

from users.models import Profile


class Fields(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    icon = models.ImageField('Иконка', upload_to='uploads/icons/', null=True)
    title = models.CharField('Навазние', max_length=20)
    value = models.CharField('Значение', max_length=100)

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Tags(models.Model):
    icon = models.ImageField('Иконка', upload_to='uploads/icons/', null=True)
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Publications(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    blog = models.BooleanField(default=True)
    text = models.TextField('Текст')
    tags = models.ManyToManyField(Tags, verbose_name='Тэги', related_name='tags')
    editDate = models.DateField('Дата редактирования', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Files(models.Model):
    publication = models.ForeignKey(Publications, related_name='publication', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/files/')

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'


class Links(models.Model):
    publication = models.ForeignKey(Publications, related_name='link_publication', on_delete=models.CASCADE)
    icon = models.ImageField('Иконка', upload_to='uploads/icons/', null=True)
    text = models.TextField('Текст')
    url = models.CharField('URL', max_length=150)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
