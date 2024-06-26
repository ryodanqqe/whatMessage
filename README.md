﻿# Project Description

This project is a script for sending messages via WhatsApp using the Twilio API, as well as for processing survey results and recording them in Google Sheets.

## Installation

1. Clone the repository to your computer:

```bash
git clone https://github.com/ryodanqqe/whatMessage.git
```

2. Install dependencies using pip
```
pip install -r requirements.txt
```

3. Make sure the `credentials.json` file for the Google Sheets API is in the project root

4. Update `contacts.json` for your needs, to test you can add your own phone number


## Usage

1. Run the script to send messages:
    ```bash
    python main.py
    ```

2. Open ngrok tunnel to local Flask server:
    ```bash
    ngrok http --domain=singular-sadly-civet.ngrok-free.app 8080
    ```

3. Your local server is now accessible via the URL provided by ngrok.
