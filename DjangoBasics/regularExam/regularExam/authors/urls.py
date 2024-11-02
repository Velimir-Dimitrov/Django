from django.urls import path

from regularExam.authors.views import AuthorCreateView, AuthorDetailsView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='author-create'),
    path('details/', AuthorDetailsView.as_view(), name='author-details'),
    path('edit/', AuthorEditView.as_view(), name='author-edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author-delete'),

]