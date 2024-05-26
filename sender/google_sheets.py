import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

yes_sheet_id = os.getenv('SHEET_ID_YES')
no_sheet_id = os.getenv('SHEET_ID_NO')

# Setting scopes
scopes = ['https://www.googleapis.com/auth/spreadsheets']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
creds_path = os.path.join(BASE_DIR, '..', 'credentials.json')

# Auth
creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
client = gspread.authorize(creds)

# Opening sheets
yes_sheet = client.open_by_key(yes_sheet_id)
no_sheet = client.open_by_key(no_sheet_id)


def write_to_yes_sheet(phone_number):
    worksheet = yes_sheet.sheet1
    worksheet.append_row([phone_number])


def write_to_no_sheet(phone_number):
    worksheet = no_sheet.sheet1
    worksheet.append_row([phone_number])


if __name__ == '__main__':
    write_to_yes_sheet(phone_number=input('Enter your phone number: '))