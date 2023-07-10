import requests
from dotenv import load_dotenv
import os
from datetime import datetime as dt

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
THANKS_CODE = os.getenv("THANKS_CODE")

GRAPH_CODING = "coding1"
GRAPH_BOOKS_READ = "books1"

PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/"
GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}graphs/"
PIXEL_ENDPOINT = f"{GRAPHS_ENDPOINT}{GRAPH_CODING}/"

DATE_STRF_FORMAT = "%Y%m%d"
DATE_STRP_FORMAT = "%d/%m/%y"


today = dt.now()
todays_date = today.strftime(DATE_STRF_FORMAT)
print(todays_date)

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}


def add_coding_hours():
    url = PIXEL_ENDPOINT
    pixel_data = {
    "date": todays_date,
    "quantity": input("How many hours of coding did you do today? "),
    }
    response = requests.post(url=url, json=pixel_data, headers=HEADERS)
    if check_status_code(code=response.status_code):
        print(f"Your hours have been added.")


def amend_coding_hours():
    date_to_amend = input("Please enter the date you would like to change in this format: YYYYmmdd ")
    url = f"{PIXEL_ENDPOINT}{date_to_amend}"
    pixel_data = {
        "date": date_to_amend,
        "quantity": input("How many hours of coding did you do on that day? ")
    }
    response = requests.put(url=url, json=pixel_data, headers=HEADERS)
    if check_status_code(code=response.status_code):
        print(f"Your hours have been amended.")


def check_status_code(code):
    if code == 200:
        return True
    else:
        print("That didn't work. Please try again.")
        return False

def delete_coding_hours():
    date_to_delete = input("Please enter the date you would like to change in this format: YYYYmmdd ")
    url = f"{PIXEL_ENDPOINT}{date_to_delete}"
    response = requests.delete(url=url, headers=HEADERS)
    if check_status_code(code=response.status_code):
        print(f"Your hours have been deleted.")


def upgrade_account():
    url = f"{PIXELA_ENDPOINT}"
    pixel_data = {
        "thanksCode": THANKS_CODE
    }
    response = requests.put(url=url, json=pixel_data, headers=HEADERS)
    if check_status_code(code=response.status_code):
        print("Your thanks code has been added to your account and you now have access to some special features.")



MENU_OPTIONS = {
    "1": add_coding_hours,
    "2": amend_coding_hours,
    "3": delete_coding_hours,
    "4": upgrade_account,
}

MENU_PROMPT = """
~~ Menu ~~

1) Record the number of hours worked on personal projects today
2) Change the number of hours worked on personal projects on a given day
3) Delete the number of hours worked on personal projects on a given day
4) Upgrade your account with a thanks code

Type 'q' to quit.

Enter your choice: """

def menu():
    while (selection := input(MENU_PROMPT).lower()) != "q":
        try: 
            MENU_OPTIONS[selection]()
        except KeyError:
            print("That's not a valid option. Please try again.")

menu()