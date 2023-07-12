import os
from dotenv import load_dotenv
import requests

load_dotenv()

SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
SHEETY_API_ENDPOINT = "https://api.sheety.co/d007e6a2913fd111e29e65a7631410e8/myWorkouts/workouts"

SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTH_TOKEN,
}


def delete_row(row_number):
    sheety_delete_endpoint = f"{SHEETY_API_ENDPOINT}/{row_number}"
    return requests.delete(url=sheety_delete_endpoint, headers=SHEETY_HEADERS)


def post_row(new_row):
    response = requests.post(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADERS, json=new_row)
    return response.status_code