import gspread
from google.oauth2.service_account import Credentials
import time
from time import sleep
from colours import QuizColours as C

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('system_junk')

user = SHEET.worksheet("user")

all_data = user.get_all_values()


def update_worksheet(data, worksheet):
    """
    Accepts a list of integer values,
    Pushes this data to the Google Spreadsheet database.
    Provides feedback of the process to the user in text format.
    """
    print(C.B + 'Quiz complete...\n')
    time.sleep(1)
    print(C.B + f"Updating '{worksheet}' data in database...\n")
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(data)
    print(C.G + f"'{worksheet}' data updated successfully.\n")