from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'death_date', 'id')

    @admin.display(description='Полное имя')
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name} {obj.second_name}'


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors')
    filter_horizontal = ['author']

    @admin.display(description='Автор')
    def get_authors(self, obj):
        return ", ".join([f'{a.first_name} {a.last_name}' for a in obj.author.all()])


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
