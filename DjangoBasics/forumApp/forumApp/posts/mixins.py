from datetime import time

from django import forms
from django.http import HttpResponseForbidden
from django.utils.timezone import localtime


class DisableFieldsMixin(forms.Form):
    disabled_field = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_field[0] == "__all__" or field_name in self.disabled_field:
                field.disabled = True


class TimeRestrictedMixin:
    start_time = time(0, 0)
    end_time = time(23, 59)
    forbidden_message = "Access restricted at this time. Please try again later."

    def dispatch(self, request, *args, **kwargs):
        current_time = localtime().time()

        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden(self.forbidden_message)

        return super().dispatch(request, *args, **kwargs)
