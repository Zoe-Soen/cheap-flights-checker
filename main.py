from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from config import *
from pprint import pprint

# ------------------------------------------------------------------
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Read current existing data from Google Spreasheet:
sheet_data = data_manager.read_existing_data("list")
values = []
values_sin_bkk = []

# ------------------------------------------------------------------
with open(MAIL_RECODE_FILE, "w+") as file:
    for destination in sheet_data:
        flight = flight_search.check_flights(
            origin_city_code = ORIGIN_CITY_IATA, 
            destination_city_code = destination["iata_code"], 
            from_time = FROM_DATE.strftime("%d/%m/%Y"), 
            to_time = SEARCH_TIMEFRAME.strftime("%d/%m/%Y"), 
            nights_in_dst_from = 7,
            nights_in_dst_to = 20,
            currency = CURRENCY
            )
        if flight == None:
            row = [
                CURRENT_DATE,  # date
                destination['city'], # city
                "-", # price
                "-", # airports
                "-", # via_city
                "-", # nights_stay
                "-", # out_departure_time
                "-", # out_stopover_arrival_time
                "-", # out_stopover_departure_time
                "-", # out_destination_arrival_time
                "-", # return_departure_time
                "-", # return_stopover_arrival_time
                "-", # return_stopover_departure_time
                "-" # return_arrival_time
            ]
            message = f"{destination['city']}: \nNo flight found today.\n\n"
            print(message)
        else:
            row = [
                CURRENT_DATE,  # date
                destination['city'], # city
                flight.price, # price
                f"{flight.origin_airport}-{flight.via_city_airport}-{flight.destination_airport}", # airports
                flight.via_city, # via_city
                flight.nights_stay, # nights_stay
                flight.out_departure_time, # out_departure_time
                flight.out_stopover_arrival_time, # out_stopover_arrival_time
                flight.out_stopover_departure_time, # out_stopover_departure_time
                flight.out_destination_arrival_time, # out_destination_arrival_time
                flight.return_departure_time, # return_departure_time
                flight.return_stopover_arrival_time, # return_stopover_arrival_time
                flight.return_stopover_departure_time, # return_stopover_departure_time
                flight.return_arrival_time # return_arrival_time
            ]
            message = f'{destination["city"]}: \n{round(flight.price,0)} JPY\n{flight.origin_airport}-{flight.destination_airport} (via: {flight.via_city})\nnights: {flight.nights_stay}\n{flight.out_departure_time} - {flight.return_departure_time}\n\n'
            print(message)
            
        values.append(row)
        file.write(message)

# Record all search results to Google Sheets: 
range_name = data_manager.get_range_name(WORKSHEET2)
data_manager.save_to_spreadsheet(values, range_name)

# Push E-MAIL Notification:              
with open(MAIL_RECODE_FILE) as data:
    message = data.read()
    notification_manager.send_mails(CURRENT_DATE, SEND_TO, message)

# # Push Mobile SMS Notification:
# notification_manager.send_sms(message)

   
