from django.urls import path

from profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailPage.as_view(), name='profile-details'),
    path('delete/', views.ProfileDeletePage.as_view(), name='profile-delete'),
]