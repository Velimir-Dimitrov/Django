from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/', views.PhotoAddPage.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditPage.as_view(), name='edit-photo'),
        path('delete/', views.delete_photo, name='delete-photo'),
    ]))
]

