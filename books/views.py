from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book  
from .serializers import BookSerializer
# Create your views here.
@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    books_json = BookSerializer(books, many=True)
    return Response (data = books_json.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show_book(request, id):
    try:
        book = Book.objects.get(pk = id)
        book_json = BookSerializer(book)
        return Response(data = book_json.data, status=status.HTTP_200_OK)
    except:
        return Response(data = {'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_book(request, id):
    try:
        book = Book.objects.get(pk = id).delete()
        return Response(data = {'message': f'Book {id} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(data = {'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

from .serializers import BookModelSerializer
@api_view(['POST'])
def create_book(request):
    try:
        json_obj = request.data
        db_obj = BookModelSerializer(data = json_obj)
        if db_obj.is_valid():
            db_obj.save()
        return Response(data = {'message': 'Book created successfully'}, status=status.HTTP_201_CREATED)
    except:
        return Response(data = {"message": "Error creating book"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_book_put(request, id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookModelSerializer(book, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': f'Book {id} updated successfully (PUT)'}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Book.DoesNotExist:
        return Response(data={'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_book_patch(request, id):
    try:
        book = Book.objects.get(pk=id)
        
        if len(request.data) != 1:
            return Response(
                data={"error": "PATCH can only update one field at a time."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        field_name = next(iter(request.data))  
        new_value = request.data[field_name]
        
        if not hasattr(book, field_name):
            return Response(
                data={"error": f"Field '{field_name}' does not exist in Book model."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        setattr(book, field_name, new_value)
        book.save()
        
        return Response(
            data={"message": f"Book {id}'s {field_name} updated to {new_value}."},
            status=status.HTTP_200_OK
        )
    
    except Book.DoesNotExist:
        return Response(
            data={"error": "Book not found."},
            status=status.HTTP_404_NOT_FOUND
        )