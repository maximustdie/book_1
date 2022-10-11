from django.urls import path

from book_files.views import FileList

app_name = 'book_files'
urlpatterns = [
    path('books/', FileList.as_view())
]