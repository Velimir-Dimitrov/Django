from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator
from django.db import models



# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            RegexValidator(
                r'^[A-Za-z]+$',
                "Your name must contain letters only!"
            )
        ],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                r'^[A-Za-z]+$',
                "Your name must contain letters only!"
            )
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            MinLengthValidator(6,"Your passcode must be exactly 6 digits!"),
            MaxLengthValidator(6, "Your passcode must be exactly 6 digits!"),
        ],
        help_text="Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )



