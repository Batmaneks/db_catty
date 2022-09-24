import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

#Fetch the sheet
sheet = client.open('DB_catty_test1').sheet1
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)