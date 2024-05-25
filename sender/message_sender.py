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


def send_messages(contact_file):
    with open(contact_file, 'r') as file:
        contacts = json.load(file)
    for contact in contacts:
        phone_number = contact['phone_number']
        message = contact['message']
        send_message(phone_number, message)


def main():
    send_messages('contacts.json')


if __name__ == '__main__':
    main()

