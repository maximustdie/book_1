from django.db import models
from book_auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    annotation = models.TextField(verbose_name='Аннотация')
    author = models.ManyToManyField(Author, verbose_name='Автор книги', related_name='books')
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    archived = models.BooleanField(default=False, verbose_name='Отправлено в архив')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Comment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    text = models.TextField(verbose_name='Текст комментария')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария',
                             related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Дата создания: {self.create_time}, Автор комментария:{self.author} Книга:{self.book}'
