from django.contrib import admin

from django_rest.books_api.models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
