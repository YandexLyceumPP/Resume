from django.db import models


class ShowManager(models.Manager):
    def get_show(self):
        return self.get_queryset().filter(show=True)


class ShowBaseModel(models.Model):
    show = models.BooleanField("Показать", default=True)

    class Meta:
        abstract = True

    objects = ShowManager()
