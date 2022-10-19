from books.celery import app
from .models import Book

@app.task
def delete_books_from_the_trash():
    Book.objects.filter(deleted=True).delete()
