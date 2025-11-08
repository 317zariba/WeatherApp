import requests
from django.conf import settings
from .forms import CityForm
from django.shortcuts import render
from django.http import HttpResponse
import random

def weather_view(request):
    weather_data = {}
    
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        if city_name:
            try:
                
                api_key = getattr(settings, 'API_KEY', 'NO_API_KEY')
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
                
                print("=" * 50)
                print(f"🔍 ОТЛАДКА:")
                print(f"Город: {city_name}")
                print(f"API Key: {api_key}")
                print(f"URL: {url}")
                
                response = requests.get(url)
                
                print(f"Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                print("=" * 50)
                
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        'city': city_name,
                        'temperature': round(data['main']['temp']),
                        'description': data['weather'][0]['description'].capitalize(),
                        'icon': data['weather'][0]['icon'],
                    }
                    print("✅ API РАБОТАЕТ! Получены реальные данные!")
                else:
                    print(f"❌ API ОШИБКА: {response.status_code}")
                    weather_types = [
                        {'temp': 25, 'desc': 'Солнечно '},
                        {'temp': 18, 'desc': 'Облачно '},
                        {'temp': 15, 'desc': 'Пасмурно '}
                    ]
                    random_weather = random.choice(weather_types)
                    weather_data = {
                        'city': city_name.upper(),
                        'temperature': random_weather['temp'],
                        'description': random_weather['desc'],
                    }
                    
            except Exception as e:
                print(f" КРИТИЧЕСКАЯ ОШИБКА: {e}")
                weather_data = {
                    'city': city_name.upper(),
                    'temperature': 20,
                    'description': f'Ошибка: {str(e)}',
                }
    
    return render(request, 'weather/index.html', {'weather_data': weather_data})