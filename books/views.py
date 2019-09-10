from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from books.serializers import BookSerializer
from .models import Book


class BooksView(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
