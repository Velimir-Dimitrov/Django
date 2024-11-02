from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

from ExamPrep.utils import get_user_obj
from albums.forms import AlbumCreateForm, AlbumDeleteForm
from albums.models import Album


# Create your views here.

class AddAlbumPage(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = "albums/album-add.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)

class DetailsAlbumPage(DetailView):
    model=Album
    pk_url_kwarg = 'id'
    template_name = "albums/album-details.html"

class EditAlbumPage(UpdateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = "albums/album-edit.html"
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


class DeleteAlbumPage(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


