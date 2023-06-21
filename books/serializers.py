from rest_framework import serializers
from books.models import Author,Book,Page

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
        
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields='__all__'