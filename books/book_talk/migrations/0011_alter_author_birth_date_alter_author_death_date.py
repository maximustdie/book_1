# Generated by Django 4.1.1 on 2022-10-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_talk', '0010_book_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата смерти'),
        ),
    ]