# Weather Alert Bot

An automated weather alert bot that monitors severe weather conditions and sends real-time SMS alerts using Python, OpenWeatherMap API, and Twilio.

## Features

- **Real-Time Alerts**: Receives SMS notifications for severe weather conditions.
- **Weather Monitoring**: Automatically checks weather data based on predefined conditions.
- **Scheduled Execution**: Runs daily using PythonAnywhere's scheduling capabilities.
- **Secure Configuration**: Protects API keys and credentials using environment variables.

## Technologies Used

- **Python**: Programming language for development.
- **OpenWeatherMap API**: For fetching current weather data and forecasts.
- **Twilio API**: For sending SMS alerts.
- **Requests**: For making API calls.
- **Logging**: For monitoring and debugging.

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/weather_alert_bot.git
3. Navigate to the project directory:
   
   ```bash
   cd weather_alert_bot
4. Install required libraries:
   
   ```bash
   pip install -r requirements.txt
5. Set up your environment variables:
   
   Create a .env file in the root directory with the following variables:
   ```makefile
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   RECIPIENT_PHONE_NUMBER=your_recipient_phone_number
   OPENWEATHER_API_KEY=your_openweather_api_key
   
## Usage

1. Run the bot:

   ```bash
   python main.py

2. The bot will check the weather and send alerts based on the conditions defined in the code.
