import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    api_key = '7e8a37017e1393d7ab5af3d7f4217732'
    url = 'https://api.openweathermap.org/data/2.5/weather'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        params = {
            'q': city.name,
            'units': 'metric',
            'appid': api_key
        }
        response = requests.get(url, params=params).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
