from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from petstagram.accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

# # Not needed since Django will check the first parameter which is email
# class AppUserLoginForm(AuthenticationForm):
#     username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'date_of_birth': 'Date of Birth:',
            'profile_picture': 'Profile Picture:',
        }