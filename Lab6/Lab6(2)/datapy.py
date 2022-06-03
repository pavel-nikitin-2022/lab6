from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

#класс для удобной записи в гугл таблицы чекните https://www.youtube.com/watch?v=caiR7WAGMVM
class GoogleSheet:
    SPREADSHEET_ID = '1uvYZlE_TCSeV3JI0t56GK0gyFndBEtPKJwFCTLk0bQY'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
 
#запись в файл введенных значений
def main(data):
   gs = GoogleSheet()
   test_range = 'List!B1:G'+ str(len(data) + 2)
   data = list(map(lambda el: [int(el)], data))
   gs.updateRangeValues(test_range, data)

if __name__ == '__main__':
    main()
