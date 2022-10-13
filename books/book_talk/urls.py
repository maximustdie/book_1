from django.urls import path, include
from rest_framework import routers
from book_talk.views import AuthorList, BookList, BookDetail, CommentList, AnswerCreate, CommentDetailViewSet


router = routers.SimpleRouter()
router.register(r'comments', CommentDetailViewSet)


app_name = 'book_talk'
urlpatterns = [

    path('author/', AuthorList.as_view()),
    path('book/<int:pk>/comments/<int:parent_id>/', AnswerCreate.as_view()),
    path('book/<int:pk>/comments/', CommentList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    path('book/', BookList.as_view()),
    path('', include(router.urls)),
]
