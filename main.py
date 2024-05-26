from flask import Flask, request

from sender.message_sender import send_messages
from sender.response_handler import process_response

app = Flask(__name__)


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.form['From']
    phone_number = from_number.split(':')[1]

    return process_response(phone_number, incoming_msg)


def main():
    send_messages()
    app.run(port=8080)


if __name__ == '__main__':
    main()

