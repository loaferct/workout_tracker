import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = '79'
HEIGHT_CM = '150'
AGE = '20'

APP_ID = '053xxxxxx'
API_KEY = '1ff37c49cab19b81a04c00xxxxxxx'
API_ACCESS_TOKEN = 'e0c12a80acef53a168ba9xxxx'
SHEET_ID = 'workouxxxxxxxx'
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f'https://api.sheety.co/{API_ACCESS_TOKEN}/{SHEET_ID}/workouts'

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    "x-app-key" : API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


response = requests.post(url = nutrition_endpoint, json = parameters, headers = headers)

result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(sheety_endpoint, json = sheet_inputs)