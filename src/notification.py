# src/notification.py
from twilio.rest import Client
from config.config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER

def send_sms(alerts):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    message_body = "\n".join(alerts)
    
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        print("SMS sent successfully!")
    except Exception as e:
        print("Failed to send SMS:", e)
