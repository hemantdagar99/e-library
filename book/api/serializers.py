from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', "author", "publish_date", "price", "id"]
        # read_only_fields = ('publish_date',)


