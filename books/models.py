from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(User):

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Authors'
    

class Book(models.Model):
    book_title=models.CharField(max_length=50)
    book_image=models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    def __str__(self):
        return self.book_title
    

class Page(models.Model):
    page_content=models.CharField(max_length=2000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='page')
    page_number=models.PositiveIntegerField()
    def __str__(self):
        return self.book

