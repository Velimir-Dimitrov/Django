from django import forms
from .models import Workout
from ..mixins import PlaceholderMixin


class WorkoutForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'category', 'duration_minutes', 'calories_burned', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
