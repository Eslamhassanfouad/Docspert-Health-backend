from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=50)
    author_email=models.CharField(max_length=100)
    def __str__(self):
        return self.author_name
    

class Book(models.Model):
    book_title=models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    def __str__(self):
        return self.book_title
    

class Page(models.Model):
    page_content=models.CharField(max_length=2000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='page')
    def __str__(self):
        return self.book
    