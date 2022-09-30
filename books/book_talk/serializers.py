from .models import Author, Book, Comment
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'annotation', 'author', 'creator_id', 'archived']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['create_time', 'update_time', 'text', ]
