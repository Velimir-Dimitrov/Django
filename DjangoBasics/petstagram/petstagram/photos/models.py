from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizeValidator


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=[
            MaxSizeValidator(5)
        ]
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10)],
        blank=True,
        null=True,
    )

    location = models.TextField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )



