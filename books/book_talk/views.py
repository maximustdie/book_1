from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorSerializer, BookSerializer
from book_talk.models import Author, Book
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from drf_yasg.utils import swagger_auto_schema


# Авторы
@method_decorator(
    name='get',
    decorator=swagger_auto_schema(operation_description="Получить список авторов с фильтрами по ФИО"
                                  ))
class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'second_name']


# Книги
@method_decorator(
    name='get',
    decorator=swagger_auto_schema(operation_description="Получить список книг с фильтрами по ФИО"
                                  ))
@method_decorator(
    name='post',
    decorator=swagger_auto_schema(operation_description="Создать книгу"
                                  ))
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author__first_name', 'author__last_name', 'author__second_name']


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(operation_description="Получить список книг с фильтрами по ФИО автора и заголовку"
                                  ))
@method_decorator(
    name='put',
    decorator=swagger_auto_schema(operation_description="Обновить экземпляр книги"
                                  ))
@method_decorator(
    name='patch',
    decorator=swagger_auto_schema(operation_description="Обновить поля экземпляра книги"
                                  ))
@method_decorator(
    name='delete',
    decorator=swagger_auto_schema(operation_description="Удалить экземпляр книги"
                                  ))
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]

