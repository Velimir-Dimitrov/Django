from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram.accounts.models import AppUser, Profile

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

class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_like_count'] = sum(p.like_set_count() for p in self.object.photo_set.all())

        return context

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')