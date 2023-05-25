import requests
from datetime import datetime
import smtplib

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
iss_position = (iss_longitude,iss_latitude)

MY_LAT = 37.765205
MY_LONG = -122.241638
FORMATTED = 0
if (iss_latitude < (MY_LAT+5) or iss_latitude > (MY_LAT-5)) and (iss_longitude < (MY_LONG+5) or iss_longitude > (MY_LONG-5)):
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted={FORMATTED}")
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                my_email = "richardjamalthefifth@gmail.com"
                password = "dqucmpllnxzbszop"
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Look UP!\n\nLOOK UP!!")

