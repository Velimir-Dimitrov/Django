from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class AlphaNumeric:
    def __init__(self, message=None):
        self.message = message or 'Ensure this value contains only letters, numbers, and underscore.'

    def __call__(self, value):
        if not re.match(r'^[\w]+$', value):
            raise ValidationError(self.message)