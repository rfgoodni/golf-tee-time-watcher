from twilio.rest import Client
import os

client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))

def send_sms(phone, message):
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_FROM"),
        to=phone
    )
