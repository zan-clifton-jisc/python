## Workout Tracker

This workout tracker uses the natural language API at [Nutritionix](https://www.nutritionix.com/) to interpret a user's prompt regarding exercise completed on a given day. Then, using the [Sheety API](https://sheety.co/), updates a worksheet in [Google Sheets](https://workspace.google.com/intl/en_uk/lp/sheets/) with the information returned from Nutritionix.

Additionally, the profile information for the user is saved in a [JSON file](https://github.com/zan-clifton-jisc/python/blob/main/02-workout-tracker/profile.json) (I make no assertions that this profile information is accurate in any way) and read in order to complete the Nutritionix query. Nutritionix will provide specific calorie information based upon the user profile.

You can [access the project on Repl](https://replit.com/@zan-clifton/Workout-Tracker?v=1) and [view the sheet](https://docs.google.com/spreadsheets/d/1LwzBlyQvx6THmuWZ2gJD7KZbvsiI7KR_PLD-Y7yZ2SU/edit?usp=sharing) to watch in real time as it updates.
