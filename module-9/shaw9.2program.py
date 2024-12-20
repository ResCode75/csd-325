#Rachel Shaw - 9.2 Assignment - 12/7/2024

import requests
import json

# GET request for API
response = requests.get("https://www.dnd5eapi.co/api/ability-scores")

# print connection status code
print(f"--CONNECTION TEST--\n{response.status_code}\n")

 # D&D 5th Edition ability scores as unformatted json 
print(f"--ABILITY SCORES JSON--\n{response.json()}\n")

print(response.json)

# Function to convert response into a formatted JSON string
def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(f'--FORMATTED JSON--\n{text}')

# print formatted D&D 5th Edition ability scores as a formatted JSON string
jprint(response.json())




