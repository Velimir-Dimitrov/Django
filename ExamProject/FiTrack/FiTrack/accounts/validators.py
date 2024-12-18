from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size:int, message=None):
        self.max_size = max_size
        self.message = message or f"File size must be below or equal to {self.max_size}MB"

    def __call__(self, value):
        max_size_bytes = self.max_size * 1024 * 1024
        if value.size > max_size_bytes:
            raise ValidationError(self.message)

def validate_image_extension(value):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
    if not value.name.split('.')[-1].lower() in valid_extensions:
        raise ValidationError("Only JPG, JPEG, PNG, and GIF files are allowed.")