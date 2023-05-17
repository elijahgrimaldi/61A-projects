import requests
MY_LAT = 37.765205
MY_LONG = -122.241638
FORMATTED = 0
from datetime import datetime
response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted={FORMATTED}")
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise,sunset)

time_now = datetime.now()
