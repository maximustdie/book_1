from .models import Author, Book, Comment
from rest_framework import serializers
from book_files.serializers import FileSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'second_name', 'birth_date', 'death_date', 'owner']


class BookSerializer(serializers.ModelSerializer):
    file = FileSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'annotation', 'author', 'owner', 'archived', 'file']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'create_time', 'update_time', 'text', 'book', 'owner']
