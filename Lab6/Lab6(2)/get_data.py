from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from visualize import main_screen

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1uvYZlE_TCSeV3JI0t56GK0gyFndBEtPKJwFCTLk0bQY'
SAMPLE_RANGE_NAME = 'List!A1:E'

# Чтение гугл таблицы как и в первой программе чекните https://www.youtube.com/watch?v=caiR7WAGMVM
def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        res = []
        for row in values:
            res.append(row[0])
            print('%s\n' % (row[0]))
        #внимение сюда по сути говорим какие поля вводить в ткинтере
        main_screen(res)
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
