from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import  BookModelSerializer


# @api_view(['GET'])
# def index(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         book = serializer.save()
#         return Response(BookSerializer(book).data, status=201)
#     return Response(serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_operations(request, pk):
#     book = Book.objects.get(pk=pk)

#     if request.method == 'GET':
#         return Response(BookSerializer(book).data)

#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=204)
    
    
    
    
# @api_view(['GET', 'POST'])
# def books(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookModelSerializer(books, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BookModelSerializer(data=request.data)
#         if serializer.is_valid():
#             book = serializer.save()
#             return Response(BookModelSerializer(book).data, status=201)
#         return Response(serializer.errors, status=400)
    
    
    
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer