import requests

url = "https://ronin.rest/origin/battleLog/ronin:aea29f8d63c9aaff3271a3f7e811edc419d8878a"
url_2 = "https://ronin.rest/origin/leaderboard/vstar?player=ronin:aea29f8d63c9aaff3271a3f7e811edc419d8878a"

payload={}
headers = {}

response = requests.request("GET", url_2, headers=headers, data=payload)


print(response.text)