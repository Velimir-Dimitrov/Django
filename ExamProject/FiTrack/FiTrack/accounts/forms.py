from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from FiTrack.accounts.models import Profile
from FiTrack.mixins import PlaceholderMixin

UserModel = get_user_model()

class AppUserLoginForm(PlaceholderMixin, AuthenticationForm):
    pass

class AppUserChangeForm(PlaceholderMixin, UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(PlaceholderMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class ProfileEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )