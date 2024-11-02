from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models
from django.forms import CharField, EmailField

from profiles.validators import AlphaNumeric


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumeric() #can be made with regex directly here / extra step with validator on separate file
        ]
    )

    email = models.EmailField()

    Age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

