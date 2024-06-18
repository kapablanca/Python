import requests
from datetime import datetime
import os

APP_ID = "7ab95397"
API_KEY = "3d7d811088b2a5cb8521a8c85c86bdfa"
SHEET_ENDPOINT = "https://api.sheety.co/628850b014bfe552f841e77bccb77bc8/workoutTracking/workouts"
USER = "test"
PASS = "test12345"

GENDER = "male"
WEIGHT = 78
HEIGHT = 178
AGE = 32




headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


exercise_config = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
record = response.json()

for exercise in record["exercises"]:
    exercise_name = exercise["name"].title()
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]
    date = datetime.now().strftime("%x")
    time = datetime.now().strftime("%X")

    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=sheety_config, auth=(USER, PASS))
    print(response.text)
