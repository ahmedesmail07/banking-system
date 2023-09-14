from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from schema_graph.views import Schema


urlpatterns = [
    path("admin/", admin.site.urls),
    path("models/", Schema.as_view()),
    path("", include("main.urls")),
    path("users/", include("users.urls")),
    path("account/", include("account.urls")),
]

# Add media root for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
