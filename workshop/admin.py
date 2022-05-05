from django.contrib import admin

from workshop.models import Tag, Publication, File, Link, Resume, Icon

admin.site.register(Icon)
admin.site.register(Resume)
admin.site.register(Tag)
admin.site.register(Publication)
admin.site.register(File)
admin.site.register(Link)
