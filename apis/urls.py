from django.urls import path

from .views import BookAPIView

urlpatterns=[
    path('',BookAPIView, name='book_list')
]