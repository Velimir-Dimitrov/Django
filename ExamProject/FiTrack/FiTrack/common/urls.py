from django.urls import path

from FiTrack.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    ]