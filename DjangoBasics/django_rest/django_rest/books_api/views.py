from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django_rest.books_api.models import Book
from django_rest.books_api.serializers import BookSerializer


# # Json return

# def index(request):
#     return JsonResponse({"name": "velimir"})

# # Regular function view
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {'books': books}
#
#     return render(request, 'some_template.html', context)

# # Json function
# def list_books_view(request):
#     books = Book.objects.all() # QuerySet
#
#     context = {'books': books}
#
#     return JsonResponse(context)
#     # Error: Object of type QuerySet is not JSON serializable
#     # parse context to Json if you want to use such function

# # For next lesson Rest advanced
# class ListBooksApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # REST function
@api_view(["GET", "POST"])
def list_books_view(request):
    if request.method == "GET":

        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer},
)


class BookViewSet(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Book, pk=pk)

    @staticmethod
    def serializer_valid(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk:int):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk:int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        return self.serializer_valid(serializer)

    def patch(self, request, pk:int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        return self.serializer_valid(serializer)

    def delete(self, request, pk:int):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)