from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from profiles.models import Profile


# Create your views here.
class ProfileDetailPage(DetailView):
    model = Profile
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return self.model.objects.first()


class ProfileDeletePage(DeleteView):
    model = Profile
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.model.objects.first()