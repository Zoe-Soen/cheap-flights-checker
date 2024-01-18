# encoding: utf-8
from datetime import datetime as dt, timedelta

# ---------------- Flight Seartch API access Info ----------------
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "" # Register your own API KEY and replace


# -------------- City-From-To / Currency / Time-Frame --------------
ORIGIN_CITY_IATA = "TYO" # Replace your departure city IATA code
CURRENCY = "JPY" # Replace the currency you prefer

CURRENT_DATE = dt.now().strftime('%Y/%m/%d')
FROM_DATE = dt.now() + timedelta(days=1)
SEARCH_TIMEFRAME = dt.now() + timedelta(days=(6 * 30))


# ------------------- Mail Notification settings -------------------
# export MAIL_SENDER=xxxxxxx@xxxx.com
# export MAIL_SENDER_PW=xxxxxxxxxxxxxxxxxxxxxx
SEND_TO = "" # To multi persons: ["email_1", "email_2",...,"email_n"]
MAIL_FOLDER = "./assets/sent_mail_records"
MAIL_RECODE_FILE = f"{MAIL_FOLDER}/{dt.now().strftime('%Y%m%d')}.txt"

# ---------------- Mobile SMS Notification settings ----------------
# export TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxxxxxxxxxx
# export TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxx
# export TWILIO_VIRTUAL_NUMBER=+0000000000
# export TWILIO_VERIFIED_NUMBER=+810000000000


# -------------------- Google Sheets API Info --------------------
GOOGLE_SHEEET_URL = "https://docs.google.com/spreadsheets/d/1Ua7jD6dcvPUoj5l_VbjmOIV7tl2Adm6OrSVQhywBzJE/edit#gid=1484169761"
SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SERVICE_ACCOUNT = "./assets/wish-list-tracer-79fea93c45dd.json"  # Replace your own Google Spreadsheet Service Account Key
SHEET_ID = "1Ua7jD6dcvPUoj5l_VbjmOIV7tl2Adm6OrSVQhywBzJE"   # Replace sheet id
WORKSHEET1 = "list" #Sheet name for the Target Cities and Maximum Allowable Prices list
WORKSHEET2 = "price_records"  # Sheet name for all search records
WORKSHEET3 = "sin-bkk" # Sheet name for search record of particular city


# ---------------------- Local record folder ----------------------
LOCAL_RECORD_FILE = f"./assets/flight-deals-start - prices.csv"
