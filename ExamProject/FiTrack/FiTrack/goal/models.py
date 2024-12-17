from django.db import models
from django.contrib.auth import get_user_model

from FiTrack.goal.validators import validate_future_date
from FiTrack.workout.models import Workout

UserModel = get_user_model()


class Goal(models.Model):
    account = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="goals"
    )

    workouts = models.ManyToManyField(
        Workout,
        related_name="goals",
        blank=True
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    target_date = models.DateField(
        validators=[
            validate_future_date
        ]
    )

    is_completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    def progress(self):
        total_calories = sum(workout.calories_burned for workout in self.workouts.all())
        return total_calories