# Generated by Django 4.1.1 on 2022-10-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_talk', '0009_remove_comment_answer_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Отправленно в корзину'),
        ),
    ]
