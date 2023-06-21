from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view  
from .models import Author,Book,Page
from .serializers import AuthorSerializer,BookSerializer,PageSerializer
from rest_framework import status,filters
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

#Please Note i'm making GET/POST 'Listing' By viewsets
class viewsets_author(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
class viewsets_book(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class viewsets_page(viewsets.ModelViewSet):
    queryset=Page.objects.all()
    serializer_class=PageSerializer
    
    
#In 'PK Method'---->GET/PUT/DELETE  i will be using Function Based View

@api_view(['GET','PUT','DELETE'])
def author(request,pk):
    data=get_object_or_404(Author,pk=pk)
    if request.method=='GET':
        serializer=AuthorSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='PUT':
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(data,serializer.data)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        data.delete()
        return Response(status.HTTP_200_OK)
    
@api_view(['GET','PUT','DELETE'])
def book(request,pk):
    data=get_object_or_404(Book,pk=pk)
    if request.method=='GET':
        serializer=BookSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='PUT':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(data,serializer.data)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        data.delete()
        return Response(status.HTTP_200_OK)
    
@api_view(['GET','PUT','DELETE'])
def page(request,pk):
    data=get_object_or_404(Page,pk=pk)
    if request.method=='GET':
        serializer=PageSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='PUT':
        serializer=PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(data,serializer.data)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        data.delete()
        return Response(status.HTTP_200_OK)
    
    

