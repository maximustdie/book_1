from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from books import settings

schema_view = get_schema_view(openapi.Info(
    title="Book API",
    default_version='v1',
    description="Зима близко",
),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('book_auth.urls', namespace='book_auth')),
    path('api/files/', include('book_files.urls', namespace='book_files')),
    path('api/', include('book_talk.urls', namespace='book_talk')),
    path('doc_api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)