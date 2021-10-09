from rest_framework import routers

from book.api import api

router = routers.DefaultRouter()

router.register(r'book', api.BookViewSet)
