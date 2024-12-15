from django import forms
from .models import Goal
from ..mixins import PlaceholderMixin


class GoalForm( PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'description', 'target_date', 'workouts']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'})
        }
