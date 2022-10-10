from django.urls import path

from book_files.views import FileView

app_name = 'book_files'
urlpatterns = [
    path('upload/', FileView.as_view())
]