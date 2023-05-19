import requests
api_key = "cf1ed49fb87485b3139aaf9f209df896"
parameters = {
    "lat" : 37.804363,
    "lon" : -122.271111,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
    }
response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()