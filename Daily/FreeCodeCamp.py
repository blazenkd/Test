# 2/14/2023
# ---FreeCodeCamp---
"""
Webservices: JSON

What will the following code print?
"""
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
