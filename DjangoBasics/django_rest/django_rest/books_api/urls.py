from django.urls import path

from django_rest.books_api import views

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),

]