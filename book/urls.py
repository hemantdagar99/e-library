
from django.urls import path, include, re_path
from .views import home, book_list, book_detail, book_create, book_delete, book_update

urlpatterns = [
    path('', home, name='home'),
    path('list/', book_list, name='book_list'),
    path('<int:id>/', book_detail, name='book_detail'),
    path('create', book_create, name='book_create'),
    path('<int:id>/delete/', book_delete, name='book_delete'),
    path('<int:id>/update/', book_update, name='book_update'),

]