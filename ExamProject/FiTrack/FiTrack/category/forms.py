from django import forms
from .models import Category
from ..mixins import PlaceholderMixin


class CategoryForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']