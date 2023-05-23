import requests
import os
from datetime import datetime
now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

GENDER = "male"
WEIGHT_KG = "90"
HEIGHT_CM = "180"
AGE = "23"
os.environ["APP_ID"]= "a6eae814"
os.environ["API_KEY"]="eba4ece5e23a65c95b0cdca910834c1d"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NUTRITION_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/45d4f359c7a03991d8ee5dc12baf8c9c/myWorkouts/workouts"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "0"
}
parameters = {

    "query" : input("What did you do today? "),
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}
nutrition_response = requests.post(url=NUTRITION_URL,json=parameters,headers=headers)
nutrition_response.raise_for_status()
exercise_data = nutrition_response.json()
exercise = exercise_data["exercises"][0]["name"]
duration = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]
sheet_params = {
    "workout":{
        "date" : date,
        "time" : time,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories
    }
}
sheet_header = {
    "Authorization" : "Bearer aoejfposemnfoinfksdfis"
}


sheet_post = requests.post(url=SHEETY_URL, json=sheet_params, headers=sheet_header)
sheet_post.raise_for_status()