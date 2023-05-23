flights_endpoint = "https://api.tequila.kiwi.com"
flights_api_key = "yDyUYxzeIqsYEZOw2yM6YUb8gGwwygvy"
import requests
from flight_data import FlightData
class FlightSearch:
    def get_flight_code(self,city):
        
        params = {
            "term" : city["city"]
        }
        header = {
            "apikey" : flights_api_key
        }

        response = requests.get(url=flights_endpoint,params=params, headers=header)
        response_data = response.json()['data'][0]
        return response_data['locations'][0]['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": flights_api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{flights_endpoint}/v2/search",headers=headers,params=query)
        #catches excepts for flights with 0 layovers, can we find a way to make this general for any amount of layovers?
        try:
            data = response.json()['data'][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{flights_endpoint}/v2/search",headers=headers,params=query)
            data = response.json()['data'][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            print(f"Low price alert! Only {flight_data.price} to fly from {flight_data.origin_city} to {flight_data.destination_city}")
            print(f"Flight has 1 stop over in {flight_data.via_city}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data

# obj = FlightSearch()
# city = {
#     "city" : "Paris"
# }
# obj.get_flight_code(city=city)

