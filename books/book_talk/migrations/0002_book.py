# Generated by Django 4.1.1 on 2022-09-30 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_auth', '0001_initial'),
        ('book_talk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('annotation', models.TextField(verbose_name='Аннотация')),
                ('creator_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('archived', models.BooleanField(default=False, verbose_name='Отправлено в архив')),
                ('author', models.ManyToManyField(related_name='books', to='book_talk.author', verbose_name='Автор книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]