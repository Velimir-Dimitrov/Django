from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from FiTrack.accounts.choices import Genders
from FiTrack.accounts.validators import MaxSizeValidator

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        choices=Genders.choices,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )

    weight = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True, null=True,
        validators = [
            MinValueValidator(15),
            MaxValueValidator(640),
        ]
    )

    height = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(30),
            MaxValueValidator(260)
        ]
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        validators=[
            MaxSizeValidator(5)
        ],
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name

        return self.first_name or self.last_name or "Anonymous"
