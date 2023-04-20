import requests
import json

url = "https://ronin.rest/origin/battleLog/ronin:aea29f8d63c9aaff3271a3f7e811edc419d8878a"
url_2 = "https://ronin.rest/origin/leaderboard/vstar?player=ronin:aea29f8d63c9aaff3271a3f7e811edc419d8878a"

payload={}
headers = {}

# Layer 0: response.json = {battles: [List]} # Dictionary
response = requests.request("GET", url, headers=headers, data=payload)
if response.status_code == 200:
    response_json = json.loads(response.text)
    keys = response_json.keys()
    # do something with the response_json
else:
    print("Error:", response.status_code)

# print(response_json)
# print(keys)

# Layer 1: battles = [{battle_uuid: _ }, {replay_url: _ }] # List of dictionaries 
battles = response_json['battles']
print(type(battles))
print(battles[0])

# Layer 2: Get each dictionary from the list

keys = set()

for d in battles:
    for k in d.keys():
        keys.add(k)

print(keys)
print(replay_url)