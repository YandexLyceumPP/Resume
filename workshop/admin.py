from typing import Text
from django.contrib import admin

from workshop.models import Tag, Resume, Icon, Block, FileInfo, TextInfo, FileConfig
# from workshop.models import Publication, File, Link, 
admin.site.register(Icon)
admin.site.register(Resume)
admin.site.register(Tag)
admin.site.register(Block)
admin.site.register(FileConfig)
admin.site.register(FileInfo)
admin.site.register(TextInfo)
# admin.site.register(Publication)
# admin.site.register(File)
# admin.site.register(Link)
