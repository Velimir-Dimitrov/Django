from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from regularExam.authors.forms import AuthorCreateForm, AuthorEditForm
from regularExam.authors.models import Author
from regularExam.common.templatetags.get_author import get_author


# Create your views here.
class AuthorCreateView(CreateView):
    model=Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

class AuthorDetailsView(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_author()




class AuthorEditView(UpdateView):
    template_name = 'authors/edit-author.html'
    model = Author
    form_class = AuthorEditForm
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_author()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author()
