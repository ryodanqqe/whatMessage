from .google_sheets import write_to_yes_sheet, write_to_no_sheet
from twilio.twiml.messaging_response import MessagingResponse


def process_response(phone_number, incoming_msg):
    response = MessagingResponse()

    if incoming_msg.lower() == 'yes':
        response.message('Thank you for your positive response!')
        write_to_yes_sheet(phone_number)
    elif incoming_msg.lower() == 'no':
        response.message('Thanks for your reply!')
        write_to_no_sheet(phone_number)
    else:
        response.message('Thank you for your message! Please answer "Yes" or "No".')

    return str(response)

