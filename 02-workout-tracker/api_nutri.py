import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_API_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}


def post_exercise(exercise_data):
    response = requests.post(url=NUTRITIONIX_API_EXERCISE_ENDPOINT, headers=NUTRITIONIX_HEADERS, json=exercise_data)
    response.raise_for_status()
    return json.loads(response.text)

