from django.contrib import admin

from workshop.models import Fields, Tags, Publications, Files, Links

admin.site.register(Fields)
admin.site.register(Tags)
admin.site.register(Publications)
admin.site.register(Files)
admin.site.register(Links)
