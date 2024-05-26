from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


def process_response(phone_number, incoming_msg):
    response = MessagingResponse()

    if incoming_msg == 'Yes':
        response.message('Thank you for your positive response!')
    elif incoming_msg == 'No':
        response.message('Thanks for your reply!')
    else:
        response.message('Thank you for your message! Please answer "Yes" or "No".')

    return str(response)


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.form['From']
    phone_number = from_number.split(':')[1]

    if incoming_msg in ["yes", "no"]:
        process_response(phone_number, incoming_msg)



if __name__ == '__main__':
    app.run(port=8080)
