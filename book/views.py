from .models import Book
from .serializer import BookSerializer
from rest_framework import generics, permissions 

# Create your views here.
## CRUD application operations
## List -> GET request
## Create -> POST request
## Retrieve -> GET request
## Update -> PUT request 
## Delete -> DELETE request

class ListBook(generics.ListAPIView):
    """ Lists all book on the database
    """
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permissions = [permissions.AllowAny]

class CreateBook(generics.CreateAPIView):
    """ Create a new book entry
    """
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permissions = [permissions.AllowAny]
    
