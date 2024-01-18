import requests
from config import *


# Keep search results from Tequila API (KIWI) :
class FlightData:

    def __init__(self, 
                price, 
                origin_city, 
                origin_airport, 
                destination_city, 
                destination_airport, 
                out_departure_time, 
                via_city,
                via_city_airport,
                out_stopover_arrival_time,
                out_stopover_departure_time,
                out_destination_arrival_time, 
                nights_stay,
                return_departure_time,
                return_stopover_arrival_time, 
                return_stopover_departure_time, 
                return_arrival_time
                ):
        self.price = round(price, 0)
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_departure_time = out_departure_time
        self.via_city = via_city
        self.via_city_airport = via_city_airport
        self.out_stopover_arrival_time = out_stopover_arrival_time 
        self.out_stopover_departure_time = out_stopover_departure_time
        self.out_destination_arrival_time = out_destination_arrival_time
        self.nights_stay = int(nights_stay)
        self.return_departure_time = return_departure_time
        self.return_stopover_arrival_time = return_stopover_arrival_time
        self.return_stopover_departure_time = return_stopover_departure_time
        self.return_arrival_time = return_arrival_time


class FlightSearch:
    
    def __init__(self):
        self.city_codes = []
    
    # Use Tequila.kiwi API to get IATA for a city: https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
    def get_destination_code_single(self, city_name):
        print("get destination codes triggered")
        url = f"{KIWI_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {"term": city_name, "location_types": "city"}
        resp = requests.get(url=url, headers=headers, params=query)
        location_data = resp.json()["locations"]
        iata_code = location_data[0]["code"]
        return iata_code 
    
    # Use Tequila.kiwi API to search and return flight results under the certain conditions:
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, nights_in_dst_from, nights_in_dst_to, currency):
        url = f"{KIWI_ENDPOINT}/v2/search"
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": nights_in_dst_from, # minimum nights
            "nights_in_dst_to": nights_in_dst_to, # maxmum nights
            "flight_type": "round",
            "one_for_city": 1,  # True for Direct Flight
            "max_stopovers": 0,  # False for stopover
            "curr": currency
        }

        resp = requests.get(url=url, headers=headers, params=query)
        data = resp.json()["data"]
        if len(data) > 0:
            flight_data = FlightData(
                price = data[0]["price"], 
                origin_city = data[0]["cityFrom"],
                origin_airport = data[0]["flyFrom"],
                destination_city = data[0]["cityTo"], 
                destination_airport = data[0]["flyTo"], 
                out_departure_time = data[0]["local_departure"].replace("T"," ").replace(":00.000Z",""), 
                via_city = "",
                via_city_airport = "",
                out_stopover_arrival_time = "",
                out_stopover_departure_time = "",
                out_destination_arrival_time = data[0]["route"][0]["local_arrival"].replace("T"," ").replace(":00.000Z",""),
                nights_stay = data[0]["nightsInDest"],
                return_departure_time = data[0]["route"][1]["local_departure"].replace("T"," ").replace(":00.000Z",""),
                return_stopover_arrival_time = "", 
                return_stopover_departure_time = "", 
                return_arrival_time = data[0]["route"][1]["local_arrival"].replace("T"," ").replace(":00.000Z",""),
            )
            return flight_data
        else:
            query["max_stopovers"] = 2
            resp = requests.get(url=url, headers=headers, params=query)
            data = resp.json()["data"]
            if len(data) > 0:
                flight_data = FlightData(
                    price = data[0]["price"], 
                    origin_city = data[0]["cityFrom"], 
                    origin_airport = data[0]["flyFrom"],
                    destination_city = data[0]["cityTo"], 
                    destination_airport = data[0]["flyTo"], 
                    out_departure_time = data[0]["local_departure"].replace("T"," ").replace(":00.000Z",""), 
                    via_city = data[0]["route"][0]["cityTo"],
                    via_city_airport = data[0]["route"][0]["flyTo"],
                    out_stopover_arrival_time = data[0]["route"][0]["local_arrival"].replace("T"," ").replace(":00.000Z",""),
                    out_stopover_departure_time = data[0]["route"][1]["local_departure"].replace("T"," ").replace(":00.000Z",""),
                    out_destination_arrival_time = data[0]["route"][1]["local_arrival"].replace("T"," ").replace(":00.000Z",""), 
                    nights_stay = data[0]["nightsInDest"],
                    return_departure_time = data[0]["route"][2]["local_departure"].replace("T"," ").replace(":00.000Z",""),
                    return_stopover_arrival_time = data[0]["route"][2]["local_arrival"].replace("T"," ").replace(":00.000Z",""), 
                    return_stopover_departure_time = data[0]["route"][3]["local_departure"].replace("T"," ").replace(":00.000Z",""), 
                    return_arrival_time = data[0]["route"][3]["local_arrival"].replace("T"," ").replace(":00.000Z","")
                )
                return flight_data
            else:
                return None

# ------------------------------------------------------------------
if __name__ == "__main__":
    obj = FlightSearch()
    # code = obj.get_destination_code_single("HongKong")
    # print(code)
    # FROM_DATE = dt.now() + timedelta(days=1)
    # print(FROM_DATE.strftime("%d/%m/%Y"))
    