import requests
import json

url = "https://api-gateway.skymavis.com/x/origin/battle-history?type=pvp&client_id=1ec9eb7e-579e-6a97-a60c-dd46969f474e&limit=5&page=1"

headers = {
    "accept": "application/json",
    "X-API-Key": "vkJvnpXL8RLdkMMKerKJQ9ND5JL9TvYH"
}

response = requests.get(url, headers=headers)

def print_all_keys(response):
    json_data = json.loads(response.text)
    for key in json_data.keys():
        print(key)

print_all_keys(response)
print(response)