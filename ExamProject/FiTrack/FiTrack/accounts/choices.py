from django.db import models

class Genders(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'