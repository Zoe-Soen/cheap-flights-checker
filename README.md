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

Sample for Mail Notification Push：
-----------------------------------------
object:
2024/01/20_Low Price Flight! (2024/01/20)

body:
More Infomation:
https://docs.google.com/spreadsheets/d/1Ua7jD6dcvPUoj5l_VbjmOIV7tl2Adm6OrSVQhywBzJE/edit#gid=1484169761
----------------------
HongKong: 
39477 JPY
HND-HKG (via: )
nights: 14
2024-02-07 01:40 - 2024-02-21 14:55

Shanghai: 
36557 JPY
NRT-PVG (via: )
nights: 7
2024-03-04 22:25 - 2024-03-12 02:20

Guangzhou: 
65625 JPY
HND-CAN (via: )
nights: 7
2024-05-24 08:50 - 2024-05-31 14:30

Taipei: 
32956 JPY
HND-TPE (via: )
nights: 12
2024-05-22 05:25 - 2024-06-03 06:45

Singapore: 
48414 JPY
NRT-SIN (via: )
nights: 15
2024-06-08 08:15 - 2024-06-23 22:15

Bangkok: 
45013 JPY
NRT-BKK (via: )
nights: 15
2024-05-24 14:25 - 2024-06-08 23:55

Honolulu: 
No flight found today.

Guam: 
84934 JPY
NRT-GUM (via: )
nights: 7
2024-07-17 17:00 - 2024-07-24 17:05

Sydney: 
149045 JPY
HND-SYD (via: )
nights: 8
2024-06-10 07:00 - 2024-06-18 20:35

Auckland: 
117325 JPY
NRT-AKL (via: )
nights: 7
2024-06-12 19:45 - 2024-06-20 10:05

Queenstown: 
149782 JPY
NRT-ZQN (via: Brisbane)
nights: 12
2024-06-03 20:50 - 2024-06-16 15:25

Paris: 
181733 JPY
HND-CDG (via: )
nights: 20
2024-01-30 22:45 - 2024-02-20 09:30

London: 
207941 JPY
HND-LHR (via: )
nights: 7
2024-02-14 09:55 - 2024-02-21 19:00

Newyork: 
150968 JPY
HND-EWR (via: Los Angeles)
nights: 19
2024-02-02 13:05 - 2024-02-21 06:47

Dubai: 
150421 JPY
NRT-DXB (via: )
nights: 12
2024-06-04 22:30 - 2024-06-17 02:40


