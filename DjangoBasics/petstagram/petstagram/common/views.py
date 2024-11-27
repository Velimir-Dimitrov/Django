from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo

from pyperclip import copy


# Create your views here.
class HomePage(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        user = self.request.user

        for photo in context['all_photos']:
            photo.has_liked = photo.like_set.filter(user=user).exists() if user.is_authenticated else False

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get("pet_name")

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset


# # Home page function view
# def home(request):
#     all_photos = Photo.objects.all()
#     comment_form = CommentForm()
#
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid():
#         all_photos = all_photos.filter(
#             tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
#         )
#
#     context = {
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#         'search_form': search_form,
#     }
#
#     return render(request, 'common/home-page.html', context)

@login_required
def like_functionality(request, photo_id):

    liked_object = Like.objects.filter(
        to_photo_id=photo_id,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

@login_required
def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()
            return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
