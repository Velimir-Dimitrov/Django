from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size:int, message=None):
        self.max_size = max_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File size must be below or equal to {self.max_size}MB"
        else:
            self.__message = value

    def __call__(self, value):
        if self.max_size * 1024 * 1024 < value.size:
            raise ValidationError(self.message)