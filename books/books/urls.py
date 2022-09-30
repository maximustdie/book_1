from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('book_auth.urls', namespace='book_auth')),
    path('api/', include('book_talk.urls', namespace='book_auth')),
]
