from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from book.api.serializers import BookSerializer
from book.models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
