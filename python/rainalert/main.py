import requests
api_key = ""
parameters = {
    "lat" : 37.804363,
    "lon" : -122.271111,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
    }
response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()