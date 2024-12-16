from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from FiTrack.accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from FiTrack.accounts.models import Profile

UserModel = get_user_model()

class AppUserLoginView(LoginView):
    template_name = 'accounts/account-login.html'
    form_class = AppUserLoginForm

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/account-create-update.html'
    success_url = reverse_lazy('home')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/account-delete.html'
    success_url = reverse_lazy('login')


class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = UserModel
    template_name = 'accounts/account-details.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/account-create-update.html'

    def get_success_url(self):
        # Dynamically return the URL based on the updated profile
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

