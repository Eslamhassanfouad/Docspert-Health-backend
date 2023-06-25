from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view  
from .models import Author,Book,Page
from .serializers import AuthorSerializer,BookSerializer,PageSerializer
from rest_framework import status,filters
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor,IsReader


#Book Classes   
class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated,IsReader,IsAuthor]
    authentication_classes=[JWTAuthentication]
    
class BookPost(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated,IsAuthor]
    authentication_classes=[JWTAuthentication]
    
    
class BookEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated,IsAuthor]
    authentication_classes=[JWTAuthentication]

  
#Page Classes
class PageList(generics.ListAPIView):
    queryset=Page.objects.all()
    serializer_class=PageSerializer
    permission_classes=[IsAuthenticated,IsAuthor,IsReader]
    authentication_classes=[JWTAuthentication]
    
class PagePost(generics.CreateAPIView):
    queryset=Page.objects.all()
    serializer_class=PageSerializer
    permission_classes=[IsAuthenticated,IsAuthor]
    authentication_classes=[JWTAuthentication]
    
class PageEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset=Page.objects.all()
    serializer_class=PageSerializer
    permission_classes=[IsAuthenticated,IsAuthor]
    authentication_classes=[JWTAuthentication]
    
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)