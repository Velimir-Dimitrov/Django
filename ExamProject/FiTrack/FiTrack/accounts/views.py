from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from FiTrack.accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from FiTrack.accounts.models import Profile
from FiTrack.mixins import PlaceholderMixin

UserModel = get_user_model()

class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('login')

    # TO DO: Login required and restriction from accessing this webpage via manually entered URL

class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/details.html'

    # TO DO: Login required

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('profile-details')

    # TO DO: Login required and restriction from accessing this webpage via manually entered URL