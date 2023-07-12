import os
from dotenv import load_dotenv
from datetime import datetime as dt
import requests
import json
from db import read_profile_data, write_profile_data
from api_nutri import post_exercise
from api_sheety import delete_row, post_row

load_dotenv()




TODAYS_DATE_FORMAT = "%d/%m/%y"
TIME_NOW_FORMAT = "%H:%M:%S"

today = dt.now()
date_today = today.strftime(TODAYS_DATE_FORMAT)
time_now = today.strftime(TIME_NOW_FORMAT)


def add_exercise():
    profile_data = read_profile_data()
    exercise_data = {
        "query": input("Describe the activities you've done today and how long they took: "),
        "gender": profile_data["gender"],
        "weight_kg": profile_data["weight_kg"],
        "height_cm": profile_data["height_cm"],
        "age": profile_data["age"]
    }
    
    exercise_response_data = post_exercise(exercise_data=exercise_data)
    exercises = exercise_response_data["exercises"]
    
    for exercise in exercises:
        new_row = {
            "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].capitalize(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
            }
        }

        if post_row(new_row=new_row) == 200:
            print("Your data has been added to the sheet.") 
       

def check_status_code(code):
    if code < 300:
        return True
    else:
        return False


def remove_row():
    row_number = input("What's the row number of the row you'd like to delete? ")
    
    response = delete_row(row_number=row_number)

    if check_status_code(code=response.status_code):
        print(f"Row {row_number} has been deleted")
    else:
        print("That didn't work. Please try again.")


def set_user_profile():
    print("""
Please note: 
Only one profile can be set at a time. 
Your profile will be stored between sessions.
Setting a new profile overwrites the existing profile.
    """)

    profile = {
        "name": input("What's your name: "),
        "weight_kg": float(input("What is your weight in Kg? ")),
        "height_cm": float(input("What is your height in cm? ")),
        "age": int(input("How old are you? ")),
        "gender": input("What's your gender? 'male'/'female' (Sorry NB sibs, it's the API) "),
    }

    write_profile_data(profile=profile)


MENU_OPTIONS = {
    "1": add_exercise,
    "2": remove_row,
    "3": set_user_profile,
}


MENU_PROMPT = """
~~ Menu ~~

1) Add today's exercise
2) Remove a row from the sheet
3) Set your profile (Required, but only once)

Type 'q' to quit.

Enter your choice: """


def menu():
    while (selection := input(MENU_PROMPT).lower()) != "q":
        try: 
            MENU_OPTIONS[selection]()
        except KeyError:
            print("That's not a valid option. Please try again.")
        except FileNotFoundError:
            print("Please set your profile first.")


menu()