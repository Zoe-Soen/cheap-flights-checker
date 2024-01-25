Cheap Flight Checker
-----------------------------------------

Function: Cheap Flight Checker
-----------------------------------------
- Specify departure city, currency, destination city (multiple), search target timeframe (up to 180 days), desired maximun price.
- Save detailed information on search results to an online Google sheet.
- Push key information such like: price, stopover, price, round trip time, to a private email.
- Push key information such like: price, stopover, price, round trip time, to SMS text message (paid).

API / Libraries:
-----------------------------------------
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

Google Sheets API settings：
-----------------------------------------
Create service account, get json key for Google sheets:
1. Open Google Cloud Platform and login: https://console.cloud.google.com/
2. Click the dropdown menu button beside "Google Cloud", click "NEW PROJECT" to create one and then select it
3. Click "API & Services" in the left menu bar, Click "+ ENABLE APIS AND SERVICES" to add APIs as below, make them enable:
   
    a. Google Sheets API >> ENABLED
   
    b. Google Drive API >> ENABLED
   
5. Click "Credentials" on the left menu bar
6. Find "Service Accounts" and click "Manage service accounts"
7. Click "+ CREATE SERVICE ACCOUNT", fill in the service account name to get an new Email address looks like: jobinfo@job-info-collector.iam.gserviceaccount.com, this is the user account for connecting your code to Google Sheet, click "CREATE AND CONTINUE"
8. Go back to the "Service Accounts" page, find your newly created email account, click "Manage keys" under "Actions" > "ADD KEY" > "Create new key" > choose key type as "JSON" > "CREATE", then you will get a downloaded json key file, rename it if you want, then save it to your project folder (mine is in the folder named "assets")
9. Go to your Google sheet, add editing privileges to this new account, save the sheet id to your code
10. Back to your project, install modules:
    pip install gspread
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
11. Import the relivant to data_manager.py:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

※Please check <gspread-manual.pdf> under assets folder.

Sample for Google online sheet:
-----------------------------------------
Please cheack: [sample] cheap_flight_checker_records.xlsx

Sample for Mail Notification Push：
-----------------------------------------
object:
2024/01/20_Low Price Flight! (2024/01/20)

body:
More Infomation:
https://docs.google.com/spreadsheets/d/1Ua7jD6dcvPUoj5l_VbjmOIV7tl2Adm6OrSVQhywBzJE/edit#gid=1484169761

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




