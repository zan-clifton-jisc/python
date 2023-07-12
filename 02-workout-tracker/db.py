import json


def read_profile_data():
    with open("profile.json", "r") as file:
        return json.load(file)
    

def write_profile_data(profile):
    json_profile = json.dumps(profile, indent=4)
    with open("profile.json", "w") as file:
        file.write(json_profile)