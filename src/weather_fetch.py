# src/weather_fetch.py
import requests
from config.config import weather_api_url

def get_weather_data():
    try:
        response = requests.get(weather_api_url)
        
        if response.status_code == 200:
            data = response.json()
            print("Weather Data:", data)
            main = data['forecast']
            weather = data['alerts'].get('alert', [])
            return {
                'forecast': main,
                'alerts': weather
            }
        else:
            print(f"Error fetching weather data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
