from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

# Create your views here.


class HomePage(TemplateView):
    template_name = 'common/project.html'

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
        API_KEY = '53f7645f3d7b2998a66680c9de6813e7'

        if not lat or not lon:
            return Response({'error': 'Latitude and longitude are required.'}, status=400)

        response = requests.get(API_URL, params={
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': 'metric',
        })
        weather_data = response.json()

        return Response({
            'location': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description']
        })