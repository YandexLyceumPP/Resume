from django.db import models


class ShowBaseModel(models.Model):
    show = models.BooleanField('Показать', default=True)

    class Meta:
        abstract = True
