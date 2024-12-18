from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from FiTrack.common import views
from FiTrack.common.views import WeatherAPIView, DashboardView, FAQViewSet, FAQPageView

router = DefaultRouter()
router.register(r'', FAQViewSet, basename='faq')

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/weather', WeatherAPIView.as_view(), name='get_weather'),
    path('faq/',FAQPageView.as_view(), name='faq-manager'),
    path('faq/api/', include(router.urls))
    ]