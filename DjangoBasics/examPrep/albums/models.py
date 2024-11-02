from django.core.validators import MinValueValidator
from django.db import models

from albums.choices import TypesOfGenre
from profiles.models import Profile


# Create your models here.

class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices= TypesOfGenre.choices,

    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[MinValueValidator(0)],
    )

    owner = models.ForeignKey(
        to=Profile, #  'profiles.Profile' can be used instead import
        on_delete=models.CASCADE,
        related_name="albums",
    )