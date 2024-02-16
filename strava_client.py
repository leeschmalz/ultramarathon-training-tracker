import requests
from pprint import pprint

# see instructions.txt to get this
access_token = ''

response = requests.get(f"https://www.strava.com/api/v3/athlete/activities?access_token={access_token}")
activities = response.json()

pprint(activities[0])