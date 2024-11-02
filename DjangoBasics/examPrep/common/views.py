from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ExamPrep.utils import get_user_obj
from albums.models import Album
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


# Create your views here.
class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if get_user_obj():
            return "profiles/home-with-profile.html"
        else:
            return "profiles/home-no-profile.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
