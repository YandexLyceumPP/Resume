from django.contrib import admin

from workshop.models import Field, Tag, Publication, File, Link

admin.site.register(Field)
admin.site.register(Tag)
admin.site.register(Publication)
admin.site.register(File)
admin.site.register(Link)
