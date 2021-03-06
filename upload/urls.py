from django.urls import path
from . import views





urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('upload', views.upload, name="upload"),
    path('books', views.book_list, name="book_list"),
    path('books/upload', views.upload_book, name="upload_book"),
    path('books/<int:pk>', views.delete_book, name="delete_book"),
    path('search', views.search, name="search"),

    path('class/books', views.BookListView.as_view(), name="class_book_list"),
    path('class/books/upload', views.UploadBookView.as_view(), name="upload_book"),
]