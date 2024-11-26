from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram.accounts.models import AppUser

UserModel = get_user_model()
# Create your views here.

class AppUserLoginView(LoginView):
    model = AppUser
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home')

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response

def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')

class ProfileEditView(UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')