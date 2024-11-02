from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from regularExam.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from regularExam.posts.models import Post
from regularExam.utils import get_author_obj


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author_id = get_author_obj().id
        return super().form_valid(form)


class PostDetailsViews(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'id'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')



class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
