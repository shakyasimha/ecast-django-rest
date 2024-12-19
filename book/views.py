from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from .models import Book
from .serializer import BookSerializer

# Create your views here.
## CRUD application operations
## List -> GET request
## Create -> POST request
## Retrieve -> GET request
## Update -> PUT request 
## Delete -> DELETE request

# class ListBook(generics.ListAPIView):
#     """ Lists all book on the database
#     """
#     queryset = Book.objects.all() 
#     serializer_class = BookSerializer 
#     permissions = [permissions.AllowAny]

# class CreateBook(generics.CreateAPIView):
#     """ Create a new book entry
#     """
#     queryset = Book.objects.all() 
#     serializer_class = BookSerializer 
#     permissions = [permissions.AllowAny]

## camelCase, PascalCase, snake_case 
## JS, C, Java, camelCase
## Python functions and variables are always written in snake_case 
## Python classes are written in PascalCase
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_book(request):
    book = Book.objects.all() 
    serializer = BookSerializer(book, many=True)
    
    if serializer is None:
        return JsonResponse(
            {
                'message': 'Empty database'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    else:
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save() 
        return JsonResponse(
            {
                'message': 'Book entry created',
                'book': serializer.data
            },
            status=status.HTTP_200_OK
        )
    else:
        return JsonResponse(
            {
                'message': 'Could not write book entry'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
## Retrieve Book entry 
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def retrieve_book_entry(request, pk):
    try: 
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Book does not exist'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = BookSerializer(book)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

## Update Book entry
@api_view(['PUT'])
@permission_classes([permissions.AllowAny])
def update_book_entry(request, pk):
    try: 
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Book does not exist'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = BookSerializer(book)
    
    if serializer.is_valid():
        serializer.save() 
        
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Delete Book Entry
@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_book_entry(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Book does not exist'
            },
            status=status.HTTP_404_NOT_FOUND
        )
        
    book.delete()
    return JsonResponse(
        {
            'message': 'Book deleted successfully.'
        },
        status=status.HTTP_204_NO_CONTENT
    )