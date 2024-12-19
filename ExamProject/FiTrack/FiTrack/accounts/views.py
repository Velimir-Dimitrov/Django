from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from FiTrack.accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from FiTrack.accounts.models import Profile
from FiTrack.mixins import SuccessMessageMixin

UserModel = get_user_model()

class AppUserLoginView(LoginView):
    template_name = 'accounts/account-login.html'
    form_class = AppUserLoginForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class AppUserRegisterView(SuccessMessageMixin, CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/account-create-update.html'
    success_url = reverse_lazy('home')
    success_message = 'Your account has been created! You can now login.'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class ProfileDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/account-delete.html'
    success_url = reverse_lazy('login')
    success_message = 'Your account has been deleted.'


class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = UserModel
    template_name = 'accounts/account-details.html'


class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/account-create-update.html'
    success_message = "Your account has been updated!"

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


