from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from FiTrack.category.models import Category
from FiTrack.workout.validators import validate_past_date

UserModel = get_user_model()

class Workout(models.Model):
    account = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="workouts"
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True, related_name="workouts"
    )

    name = models.CharField(max_length=255)

    duration_minutes = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Duration must be at least 1 minute."),
            MaxValueValidator(1440, message="Duration cannot exceed 1440 minutes (24 hours).")
        ]
    )

    calories_burned = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Calories burned must be at least 1."),
            MaxValueValidator(10000, message="Calories burned cannot exceed 10,000.")
        ]
    )

    description = models.TextField(blank=True, null=True)

    date = models.DateField(
        validators=[
            validate_past_date
        ]
    )

    def __str__(self):
        return self.name