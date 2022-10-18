from .models import Author, Book, Comment
from rest_framework import serializers
from book_files.serializers import FileSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'second_name', 'birth_date', 'death_date', 'owner']


class BookSerializer(serializers.ModelSerializer):
    file_data = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'annotation', 'author', 'owner', 'archived', 'file', 'file_data', 'deleted']

    def get_file_data(self, obj):
        if obj.file:
            return FileSerializer(obj.file).data
        return None


class CommentSerializer(serializers.ModelSerializer):
    daughter_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'create_time', 'update_time', 'text', 'book', 'owner', 'daughter_comment', 'parent']

    def get_daughter_comment(self, obj):
        queryset = Comment.objects.filter(parent_id=obj.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data
