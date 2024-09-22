# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY_NAME = os.getenv('CITY_NAME')
BASE_URL = os.getenv('BASE_URL')

weather_api_url = f"{BASE_URL}key={API_KEY}&q={CITY_NAME}&alerts=yes"

ALERT_CONDITIONS = {
    'high_temperature': 10,
    'low_temperature': 0,
    'storm_warning': ['storm', 'hurricane', 'tornado'],
    'rain_threshold': 10
}

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')
