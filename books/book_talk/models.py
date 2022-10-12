from django.db import models
from django.utils.datetime_safe import date

from book_auth.models import User
from book_files.models import File


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    second_name = models.CharField(max_length=30, verbose_name='Отчество', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True)
    death_date = models.DateField(verbose_name='Дата смерти', blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    annotation = models.TextField(verbose_name='Аннотация')
    author = models.ManyToManyField(Author, verbose_name='Автор книги', related_name='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='books')
    archived = models.BooleanField(default=False, verbose_name='Отправлено в архив')
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='Файл', related_name='books', null=True,
                             blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Comment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    text = models.TextField(verbose_name='Текст комментария')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария',
                              related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='comments')
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, verbose_name='Ответил', related_name='daughter',
                               default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'id:{self.id} Дата создания: {self.create_time} // Пользователь:{self.owner} // Книга:{self.book}'
