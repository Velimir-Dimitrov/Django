from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("The goal date cannot be in the past.")