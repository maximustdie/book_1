"""
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

# you can change the name here
app = Celery("books")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'delete-books-every-twelve-hourse': {
        'task': 'book_talk.tasks.delete_books_from_the_trash',
        'schedule': crontab(minute=0, hour='*/12'),
    },
}

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks()

@app.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y
