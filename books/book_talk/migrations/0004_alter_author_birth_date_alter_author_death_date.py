# Generated by Django 4.1.1 on 2022-10-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_talk', '0003_alter_author_second_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True, verbose_name='Дата смерти'),
        ),
    ]
