# main.py
from dotenv import load_dotenv
from src.alert_conditions import check_alerts, send_sms
from src.weather_fetch import get_weather_data

# Load environment variables
load_dotenv()

def main():
    weather_data = get_weather_data()
    print("Weather Data:", weather_data)

    if weather_data:
        alerts = check_alerts(weather_data)
        
        print("Alerts Found:", alerts)

        if alerts:
            send_sms(alerts)
        else:
            print("No alerts to send.")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
