from django.urls import path

from book_talk.views import AuthorList, BookList, BookDetail, CommentList, CommentUpdate, CommentDestroy, AnswerCreate

app_name = 'book_talk'
urlpatterns = [
    path('author/', AuthorList.as_view()),
    path('book/<int:pk>/comments/<int:parent_id>/', AnswerCreate.as_view()),
    path('book/<int:pk>/comments/', CommentList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    path('book/', BookList.as_view()),
    path('comment/<int:pk>/delete/', CommentDestroy.as_view()),
    path('comment/<int:pk>/', CommentUpdate.as_view()),
]
