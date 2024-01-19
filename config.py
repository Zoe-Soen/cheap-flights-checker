# encoding: utf-8
from datetime import datetime as dt, timedelta


# ---------------- Flight Seartch API access Info ----------------
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"


# -------------- City-From-To / Currency / Time-Frame --------------
ORIGIN_CITY_IATA = "TYO" # Replace your departure city IATA code
CURRENCY = "JPY" # Replace the currency you prefer

CURRENT_DATE = dt.now().strftime('%Y/%m/%d')
FROM_DATE = dt.now() + timedelta(days=1)
SEARCH_TIMEFRAME = dt.now() + timedelta(days=(6 * 30))


# ------------------- Mail Notification settings -------------------
MAIL_FOLDER = "./assets/sent_mail_records"
MAIL_RECODE_FILE = f"{MAIL_FOLDER}/{dt.now().strftime('%Y%m%d')}.txt"


# -------------------- Google Sheets API Info --------------------
SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SERVICE_ACCOUNT = "./assets/wish-list-tracer-79fea93c45dd.json"  # Replace your own Google Spreadsheet Service Account Key
SHEET_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"   # Replace sheet id
GOOGLE_SHEEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
WORKSHEET1 = "list" #Sheet name for the Target Cities and Maximum Allowable Prices list
WORKSHEET2 = "price_records"  # Sheet name for all search records
WORKSHEET3 = "sin-bkk" # Sheet name for search record of particular city

