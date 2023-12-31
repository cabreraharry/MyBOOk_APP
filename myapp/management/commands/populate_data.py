from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from faker import Faker
from myapp.models import Author, Book, Publisher, Reviewer, Magazine

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.populate_authors()
        self.populate_books()
        self.populate_publishers()
        self.populate_reviewers()
        self.populate_magazines()
        self.stdout.write(self.style.SUCCESS('Dummy data has been successfully populated.'))

    def populate_authors(self):
        for _ in range(5):
            Author.objects.create(name=fake.name())

    def populate_books(self):
        authors = Author.objects.all()
        for _ in range(20):
            Book.objects.create(
                title=fake.word(),
                published_date=fake.date_this_decade(),
                author=fake.random_element(authors),
            )

    def populate_publishers(self):
        books = Book.objects.all()
        for _ in range(3):
            publisher = Publisher.objects.create(name=fake.company())
            publisher.books.set(fake.random_elements(books, length=fake.random_int(5, 15)))

    def populate_reviewers(self):
        books = Book.objects.all()
        for _ in range(5):
            reviewer = Reviewer.objects.create(name=fake.name())
            reviewer.books_reviewed.set(fake.random_elements(books, length=fake.random_int(5, 15)))

    def populate_magazines(self):
        authors = Author.objects.all()
        for _ in range(3):
            magazine = Magazine.objects.create(
                title=fake.word(),
                publication_date=fake.date_this_decade(),
            )
            magazine.editors.set(fake.random_elements(authors, length=fake.random_int(1, 3)))
