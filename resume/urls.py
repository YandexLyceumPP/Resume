from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    # app
    path('', include('homepage.urls', namespace='homepage')),
    path('user/', include('users.urls', namespace='users')),
    path('about/', include('about.urls', namespace='about')),
    path('workshop/', include('workshop.urls', namespace='workshop')),

    # main
    path('admin/', admin.site.urls),

    # install
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
