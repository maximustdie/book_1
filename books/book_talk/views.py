from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer, BookSerializer
from book_talk.models import Author, Book
from rest_framework import status, generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Авторы
# class AuthorList(APIView):
#     """
#     Получение списка авторов и создание автора.
#     """
#     permission_classes = (permissions.IsAuthenticated,)
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['first_name', 'last_name', 'second_name']
#
#     def get(self, request, format=None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.initial_data['owner'] = self.request.user.id
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'second_name']


# class AuthorDetail(APIView):
#     """
#     Получение автора, обновление, удаление.
#     """
#     permission_classes = (IsOwnerOrReadOnly,)
#
#     def get_object(self, author_id):
#         try:
#             author = Author.objects.get(pk=author_id)
#             self.check_object_permissions(self.request, author)
#             return author
#         except Author.DoesNotExist:
#             raise Http404
#
#     def get(self, request, author_id, format=None):
#         author = self.get_object(author_id)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
#
#     def put(self, request, author_id, format=None):
#         author = self.get_object(author_id)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, author_id, format=None):
#         author = self.get_object(author_id)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Книги
# class BookList(APIView):
#     """
#     Получение списка авторов и создание автора.
#     """
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookSerializer(data=request.data)
#         serializer.initial_data['owner'] = self.request.user.id
#         if serializer.is_valid():
#
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author__first_name', 'author__last_name', 'author__second_name']


class BookDetail(APIView):
    """
    Получение книги, обновление, удаление.
    """
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            self.check_object_permissions(self.request, book)
            return book
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, book_id, format=None):
        book = self.get_object(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id, format=None):
        book = self.get_object(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id, format=None):
        book = self.get_object(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


