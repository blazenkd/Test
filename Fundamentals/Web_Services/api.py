# 2/16/2023
# ---FreeCodeCamp---
"""
Webservices: API

Application Program Interface:

The API itself is largely abstract in that it specifies an interface and controls the behavior of
the objects specified in that interface. The software that provides the functionality described
by an API is said to be an "implementation" of the API. An API is typically defined in terms of
the programming language used to build an application
"""
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
  address = input('Enter location: ')
  if len(address) < 1: break

  url = serviceurl + urllib.parse.urlencode({'address': address})
  print('Retrieving', url)
  uh = urllib.request.urlopen(url)
  data = uh.read().decode()
  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data)
  except:
    js = None
  
  if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failur to Retrieve ====')
    print(data)
    continue

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
"""
API Security and Rate Limiting
  # The compute resources to run these APIs are not "free"
  # The data provided by these APIs is usually valuable
  # The data providers might limit the number of requests per day,
  demand an API "key", or even charge for usage
  # The might change the rules as things progress...
"""



# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
