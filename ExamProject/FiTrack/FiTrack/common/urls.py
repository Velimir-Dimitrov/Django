from django.shortcuts import render
from django.urls import path

from FiTrack.common import views
from FiTrack.common.views import WeatherAPIView


def weather_page(request):
    return render(request, 'common/weather.html')
urlpatterns = [
    path('api/weather', WeatherAPIView.as_view(), name='get_weather'),
    path('', views.HomePage.as_view(), name='home'),
    ]