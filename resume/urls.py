from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

handler404 = "homepage.views.error_404"

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
    # other
    url(r"^media/(?P<path>.*)$", serve,
        {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve,
        {"document_root": settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
