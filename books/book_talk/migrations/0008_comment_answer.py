# Generated by Django 4.1.1 on 2022-10-11 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_talk', '0007_alter_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_pre', to='book_talk.comment', verbose_name='Ответ'),
        ),
    ]