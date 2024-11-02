from django.contrib import admin
from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_publication', 'names_of_all_tagged_pets']

    @staticmethod
    def names_of_all_tagged_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagged_pets.all())