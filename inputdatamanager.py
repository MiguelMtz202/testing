import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('stellar-sunrise-280603-6399f07b2c66.json',scope)
client = gspread.authorize(creds)

fileName = 'Variables del Reporte'
sheet = client.open(fileName).sheet1

class InputDataManager:
    currentCount = 0
    array = (sheet.get_all_records())
    newDictionary = {}
    for i in array:
        _dictInArray = array[currentCount]
        variableName = _dictInArray.get('Variable')
        variableValue = _dictInArray.get('Value')
        newDictionary[variableName] = variableValue
        currentCount += 1