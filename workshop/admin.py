from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from workshop.models import Tag, Resume, Block, File, Text, Contact


class TextInlined(admin.TabularInline):
    model = Text


class BlockAdmin(OrderedModelAdmin):
    list_display = ("title", "move_up_down_links")
    inlines = (TextInlined, )


admin.site.register(Block, BlockAdmin)

admin.site.register(Contact)
admin.site.register(Resume)
admin.site.register(Tag)
admin.site.register(File)
