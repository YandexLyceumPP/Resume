from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # app
    path("", include("homepage.urls", namespace="homepage")),
    path("user/", include("users.urls", namespace="users")),
    path("about/", include("about.urls", namespace="about")),
    path("workshop/", include("workshop.urls", namespace="workshop")),
    # main
    path("admin/", admin.site.urls),
    # install
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
