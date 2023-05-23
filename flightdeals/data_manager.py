import requests
class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/45d4f359c7a03991d8ee5dc12baf8c9c/flightDeals/prices"
        self.data = {}
    def get_data(self):
        data_response = requests.get(url=self.SHEETY_ENDPOINT)
        data_response.raise_for_status()
        self.data = data_response.json()["prices"]
        return self.data

    def update_data(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
    
    def get_customer_emails(self):

        customers_endpoint = self.SHEETY_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data