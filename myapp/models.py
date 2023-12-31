from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(BaseModel):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Publisher(BaseModel):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='publishers')

    def __str__(self):
        return self.name

class Reviewer(BaseModel):
    name = models.CharField(max_length=255)
    books_reviewed = models.ManyToManyField(Book, related_name='reviewers')

    def __str__(self):
        return self.name

class Magazine(BaseModel):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    editors = models.ManyToManyField(Author, related_name='edited_magazines')

    def __str__(self):
        return self.title
