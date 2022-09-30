from django.urls import path

from book_talk.views import AuthorList, AuthorDetail

app_name = 'book_talk'
urlpatterns = [
    path('author/<int:author_id>', AuthorDetail.as_view()),
    path('author/', AuthorList.as_view()),
]