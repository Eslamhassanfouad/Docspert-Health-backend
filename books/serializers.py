from .models import Author,Book,Page
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    def create(self, validation_data):
        password = validation_data.pop('password', None) 
        instance = self.Meta.model(**validation_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields='__all__'