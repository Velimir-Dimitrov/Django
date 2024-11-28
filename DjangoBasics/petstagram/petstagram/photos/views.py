from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.
class PhotoAddPage(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = "photos/photo-add-page.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        return super().form_valid(form)


# # Photo add function view
# def add_photo(request):
#     form = PhotoAddForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)

class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = "photos/photo-details-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all()
        context["likes"] = self.object.like_set.all()
        context["comment_form"] = CommentForm()

        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()

        return context



# # Photo details function view
# def photo_details(request, pk:int):
#     photo = Photo.objects.get(pk=pk)
#     likes = photo.like_set.all()
#     comments = photo.comment_set.all()
#
#     comment_form = CommentForm()
#
#     context = {
#         'photo':photo,
#         'likes':likes,
#         'comments':comments,
#         'comment_form':comment_form
#     }
#
#     return render(request, 'photos/photo-details-page.html', context)

class PhotoEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = "photos/photo-edit-page.html"

    def test_func(self):
        photo = get_object_or_404(Photo, slug=self.kwargs['pk'])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy("photo-details", kwargs={"pk": self.object.pk})



# # Photo Edit function view
# def edit_photo(request, pk:int):
#     photo = Photo.objects.get(pk=pk)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('photo-details', pk)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'photos/photo-edit-page.html', context)

@login_required
def delete_photo(request, pk:int):
    photo =  Photo.objects.get(pk=pk)
    if request.user == photo.user:
        photo.delete()

    return redirect('home')
