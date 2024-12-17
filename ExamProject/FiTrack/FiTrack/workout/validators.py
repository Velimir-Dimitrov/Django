from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_past_date(value):
    if value > timezone.now().date():
            raise ValidationError({"Workout date cannot be in the future."})