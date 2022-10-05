from django.http import Http404
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorSerializer, BookSerializer, CommentSerializer
from book_talk.models import Author, Book, Comment
from rest_framework import generics, status
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsOwnerCommentOrOwnerBook
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


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

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.initial_data['owner'] = self.request.user.id
        if serializer.is_valid():
            serializer.save()
            return super(BookList, self).create(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# Комментарии
class CommentList(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        name='get',
        responses={200: CommentSerializer},
        operation_description="Показать список комментариев к книге"
    )
    def get(self, request, pk, format=None):
        comments = Comment.objects.filter(book=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        name='post',
        request_body=CommentSerializer,
        operation_description="Добавить комментарий к книге"
    )
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        serializer.initial_data['owner'] = self.request.user.id
        serializer.initial_data['book'] = pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdate(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        name='put',
        request_body=CommentSerializer,
        operation_description="Изменить комментарий к книге"
    )
    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        print(comment.owner)
        serializer.initial_data['owner'] = comment.owner.id
        serializer.initial_data['book'] = comment.book.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(
    name='delete',
    decorator=swagger_auto_schema(operation_description="Удалить комментарий",
                                  responses={204: CommentSerializer},
                                  ))
class CommentDestroy(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerCommentOrOwnerBook,)
