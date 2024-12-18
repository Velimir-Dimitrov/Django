from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from rest_framework.viewsets import ModelViewSet

from FiTrack.common.models import FAQ
from FiTrack.common.serializers import FAQSerializer
from FiTrack.settings import WEATHER_API_TOKEN
from FiTrack.workout.models import Workout
from FiTrack.goal.models import Goal



class HomePage(TemplateView):

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index_logged_out.html']


class WeatherAPIView(APIView):
    def get(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        API_URL = 'https://api.openweathermap.org/data/2.5/weather'
        API_KEY = WEATHER_API_TOKEN

        if not lat or not lon:
            return Response({'error': 'Latitude and longitude are required.'}, status=400)

        response = requests.get(API_URL, params={
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': 'metric',
        })
        weather_data = response.json()

        icon_code = weather_data['weather'][0]['icon']

        return Response({
            'location': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': icon_code
        })


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "common/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Aggregate data
        total_workouts = Workout.objects.filter(account=user).count()
        total_calories = Workout.objects.filter(account=user).aggregate(
            total=Sum('calories_burned')
        )['total'] or 0

        recent_workouts = Workout.objects.filter(account=user).order_by('-date')[:5]
        active_goals = Goal.objects.filter(account=user, is_completed=False)
        favorite_category = (
            Workout.objects.filter(account=user)
            .values('category__name')
            .annotate(count=Count('category'))
            .order_by('-count')
            .first()
        )

        # Prepare context
        context.update({
            'user': user,
            'total_workouts': total_workouts,
            'total_calories': total_calories,
            'recent_workouts': recent_workouts,
            'active_goals': active_goals,
            'favorite_category': favorite_category.get('category__name') if favorite_category else 'N/A',
        })
        return context

class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]

class FAQPageView(TemplateView):
    template_name = 'common/faq-manager.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = FAQ.objects.all()  # Pass FAQ data to your template
        return context