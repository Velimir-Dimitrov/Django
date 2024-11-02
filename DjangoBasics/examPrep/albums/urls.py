from django.urls import path, include

from albums import views

urlpatterns = [
    path('add/', views.AddAlbumPage.as_view(), name='album-add'),
    path('<int:id>/', include([
        path('details/', views.DetailsAlbumPage.as_view(), name='album-details'),
        path('edit/', views.EditAlbumPage.as_view(), name='album-edit'),
        path('delete/', views.DeleteAlbumPage.as_view(), name='album-delete'),
    ])),
]