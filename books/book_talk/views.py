from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer
from book_talk.models import Author
from rest_framework import status


class AuthorList(APIView):
    """
    Получение списка авторов и создание автора.
    """

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    pass
