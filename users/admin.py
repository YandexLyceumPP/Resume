from django.contrib import admin

from users.models import Profile, Skill, Field

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Field)
