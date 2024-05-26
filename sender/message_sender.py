import os
import json
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

from_number = os.getenv('TWILIO_WHATSAPP_NUMBER')


def send_message(to_number, body):
    message = client.messages.create(
        from_=from_number,
        body=body,
        to=to_number
    )


def send_messages():
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
    for contact in contacts:
        send_message(contact['phone_number'], contact['message'])


if __name__ == '__main__':
    send_messages()