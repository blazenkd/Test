# 2/17/2023
# ---FreeCodeCamp---
"""
Web Services: API Rate Limiting and Security

The compute resources to run these APIs are not "free"
The data provided by these APIs are usually valuable
The data providers might limit the number of requests per day,
demand an API "key", or even charge for usage.
They  might change the rules as things progress...

"""
import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
  print('')
  acct = input("Enter Twitter Account: ")
  if (len(acct) < 1): break
  url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': "5"})
  print('Retrieving', url)
  connection = urllib.request.urlopen(url)
  data = connection.read().decode()
  headers = dict(connection.getheaders())
  print('Remaining', headers['x-rate-limit-remaining'])
  js = json.loads(data)
  print(json.dumps(js, indent=4))

for u in js['users']:
  print(u['screen_name'])
  s = u['status']['text']
  print(' ', s[:50])

"""
Service Oriented Architecture - allows an application
to be broken into parts and distributed across a network.

An application program interface (API) is a contract
for interaction.

Web Services provide infrastructure for applications
cooperating (an API) over a network - SOAP and REST are 
two styles of web services.

XML and JSON are serialzation formats
"""

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
