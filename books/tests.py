from django.test import TestCase

from django.urls import reverse
from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle= "An excellent subtitle",
            author= "BSM",
            isbn= "1234545"
        )
    def test_book_content(self):
        self.assertEqual(self.book.title,"A good title" )
        self.assertEqual(self.book.subtitle,"An excellent subtitle" )
        self.assertEqual(self.book.author,"BSM" )
        self.assertEqual(self.book.isbn,"1234545" )