import json


def load_profiles():

    with open("student_profiles.json", "r") as file:

        profiles = json.load(file)

    return profiles