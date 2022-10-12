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
    daughter_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'create_time', 'update_time', 'text', 'book', 'owner', 'daughter_comment']

    def get_daughter_comment(self, obj):
        queryset = Comment.objects.filter(parent_id=obj.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data
