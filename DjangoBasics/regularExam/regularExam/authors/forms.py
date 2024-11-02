from django import forms

from regularExam.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('info', 'image_url')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'passcode': 'Passcode',
            'pets_number': 'Pets Number',
            'info': 'Info:',
            'image_url': 'Profile Image URL',
        }

class AuthorCreateForm(AuthorBaseForm):
    pass

class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ('passcode',)