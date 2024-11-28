from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.accounts.models import Profile
from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetBaseForm, PetAddForm, PetDeleteForm, PetEditForm
from petstagram.pets.models import Pet

# Create your views here.
class PetAddPage(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = "pets/pet-add-page.html"

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

# # Function add view
# def pet_add(request):
#     form = PetAddForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


class PetDetailsPage(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = "pets/pet-details-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['all_photos'] = self.object.photo_set.all()

        all_photos = context['pet'].photo_set.all()

        for photo in all_photos:
            photo.has_liked = photo.like_set.filter(user=self.request.user).exists()

        context['all_photos'] = all_photos

        return context

# # Function details view
# def pet_details(request, username:str, pet_slug:str):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class PetEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pet
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"
    form_class = PetEditForm

    def get_success_url(self):
        return reverse_lazy(
            "pet-details",
            kwargs={
                "username": self.kwargs.get("username"),
                "pet_slug": self.object.slug
            }
        )

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['pet_slug'])
        return self.request.user == pet.user

# # Function edit view
# def pet_edit(request, username:str, pet_slug:str):
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetAddForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('pet-details', username, pet_slug)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = "pets/pet-delete-page.html"
    slug_url_kwarg = "pet_slug"

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

    def get_initial(self):
        return self.object.__dict__

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['pet_slug'])
        return self.request.user == pet.user



# # Function delete view
# def pet_delete(request, username:str, pet_slug:str):
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#     form = PetDeleteForm(instance=pet)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)
