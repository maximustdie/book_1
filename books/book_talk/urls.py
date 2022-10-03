from django.urls import path

from book_talk.views import AuthorList, BookList, BookDetail

app_name = 'book_talk'
urlpatterns = [
    # path('author/<int:author_id>', AuthorDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('book/<int:book_id>', BookDetail.as_view()),
    path('book/', BookList.as_view()),
]