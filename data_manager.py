import os
from dotenv import load_dotenv
from flight_search import FlightSearch
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import *


# Managing flight records data by Google Speadsheet API:
class DataManager:
    def __init__(self):
        load_dotenv()
        self.service_account = (f'{os.getenv('PARENT_FOLDER')}/{os.getenv('SERVICE_ACCOUNT')}')

        self.destination_data = []
        self.flight_search = FlightSearch()
        
        # Connect to online Google Sheet：
        self.credentials = service_account.Credentials.from_service_account_file(
            filename = self.service_account,
            scopes = [SCOPE]
        )
        self.service = build('sheets', "v4", credentials=self.credentials)
        self.list_sheets_id = WORKSHEET1
        self.price_records_sheet_id = WORKSHEET2
        
    # Read current existing search records from Google Sheets:
    def read_existing_data(self, worksheet):
        """
            Data Format:
            [
                {'city': 'Shanghai', 'iata_code': 'SHA', 'lowest_price': 55000.0}, 
                {'city': 'Guangzhou', 'iata_code': 'CAN', 'lowest_price': 60000.0}, 
                {'city': 'Guilin', 'iata_code': 'KWL', 'lowest_price': 70000.0}
            ]
        """
        result = self.service.spreadsheets().values().get(
            spreadsheetId = SHEET_ID,
            range = f"{worksheet}!A1:Z" 
        ).execute()
        
        # Set values as [] empty when there's no data in rows:
        rows = result.get("values", [])   
        header = rows[0]
        
        # Using zip() mathod to ensure the data sort of for every row keeps the same as Google Sheets:
        self.destination_data = [dict(zip(header, row)) for row in rows[1:]]
        return self.destination_data
    
    # Save the latest search results to Google Sheets:
    # 1. Find out the 1st empty row:
    def get_range_name(self, worksheet):
        range_to_be_checked = f'{worksheet}!A1:Z'
        result = self.service.spreadsheets().values().get(
            spreadsheetId = SHEET_ID,
            range=range_to_be_checked
        ).execute()
        start_row_no = len(result.get("values", []))
        new_range_name = f'{worksheet}!A{start_row_no+1}:Z'
        return new_range_name
    
    # 2. Save search results to Google Sheets:
    def save_to_spreadsheet(self, values, range_name):
        try:
            values = values
            data = []
            for row in values:
                data.append(row)
            body = {
                "majorDimension" : "ROWS",
                "values": data
            }
            result = self.service.spreadsheets().values().update(
                spreadsheetId = SHEET_ID,
                valueInputOption = "USER_ENTERED",
                range = range_name,
                body = body
            ).execute()
            print(f'{result.get("updatedCells")} cells updated.')
        except HttpError as error:
            print(f'An error occurred: {error}')

# ================================================================
if __name__ == "__main__":
    data_manager = DataManager()
