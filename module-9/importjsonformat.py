import json
import requests

def jprint(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://dnd5eapi.co/api/conditions/blinded")
jprint(response.json())