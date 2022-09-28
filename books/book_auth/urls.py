from django.urls import path

from .views import RegistrationAPIView

app_name = 'book_auth'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]