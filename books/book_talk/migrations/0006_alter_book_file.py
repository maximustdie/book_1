# Generated by Django 4.1.1 on 2022-10-10 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_files', '0001_initial'),
        ('book_talk', '0005_book_file_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_files.file', verbose_name='Файл'),
        ),
    ]