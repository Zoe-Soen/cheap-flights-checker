Cheap Flight Checker

Function: Cheap Flight Checker
- Specify departure city, currency, destination city (multiple), search target timeframe (up to 180 days), desired maximun price.
- Save detailed information on search results to an online Google sheet.
- Push key information such like: price, stopover, price, round trip time, to a private email.
- Push key information such like: price, stopover, price, round trip time, to SMS text message (paid).

API / Libraries:
1. Tequila API (KIWI): for air ticket searching
    - URL: "https://tequila-api.kiwi.com"
    - Registration is required to get API_KEY.
2. Google Spreadsheet API: used to save search results to online documents.
    - from google.oauth2 import service_account
    - from googleapiclient.discovery import build
    - from googleapiclient.errors import HttpError
3. smtplib: used for push email
    - import smtplib
4. twilio: for SMS push (paid)
    - from twilio.rest import Client
