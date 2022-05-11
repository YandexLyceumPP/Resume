from django.contrib import admin

from workshop.models import Tag, Resume, Icon, Block, File, Text, FileConfig, Contact


class TextInlined(admin.TabularInline):
    model = Text


class BlockAdmin(admin.ModelAdmin):
    inlines = (TextInlined, )


admin.site.register(Block, BlockAdmin)

admin.site.register(Contact)
admin.site.register(Icon)
admin.site.register(Resume)
admin.site.register(Tag)
admin.site.register(FileConfig)
admin.site.register(File)
