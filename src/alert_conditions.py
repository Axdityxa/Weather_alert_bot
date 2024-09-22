# src/alert_conditions.py
from config.config import ALERT_CONDITIONS, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER
from twilio.rest import Client
import logging

# Initialize Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms(message):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        logging.info("SMS sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

def check_alerts(weather_data):
    alerts = []
    
    forecast = weather_data.get('forecast', {}).get('forecastday', [{}])[0].get('day', {})
    if not forecast:
        logging.warning("No forecast data available.")
        return alerts

    current_temp = forecast.get('avgtemp_c')

    if current_temp is not None:
        if current_temp > ALERT_CONDITIONS['high_temperature']:
            alert_message = f"Temperature is too high: {current_temp}°C"
            alerts.append(alert_message)
            send_sms(alert_message)
        elif current_temp < ALERT_CONDITIONS['low_temperature']:
            alert_message = f"Temperature is too low: {current_temp}°C"
            alerts.append(alert_message)
            send_sms(alert_message)
    else:
        logging.warning("Current temperature data is missing.")

    # Check for weather alerts
    weather_alerts = weather_data.get('alerts', [])
    print("Weather Alerts:", weather_alerts)
    
    if isinstance(weather_alerts, list):
        for alert in weather_alerts:
            description = alert.get('description', '').lower()
            for storm_keyword in ALERT_CONDITIONS['storm_warning']:
                if storm_keyword in description:
                    alert_message = f"Storm warning: {description}"
                    alerts.append(alert_message)
                    send_sms(alert_message)
    else:
        logging.warning("No alerts available or alerts are not in the expected format.")

    return alerts
