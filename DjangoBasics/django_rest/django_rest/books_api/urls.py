from django.urls import path

from django_rest.books_api import views

urlpatterns = [
    path('', views.index, name='index'),
]