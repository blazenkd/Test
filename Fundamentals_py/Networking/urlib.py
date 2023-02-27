# 2/14/2023
# ---FreeCodeCamp---
"""
What will the output of the following code be like?:
"""
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""
So, I can now get website data
"""
import urllib.request
fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Hotel_del_Luna')
for line in fhand:
    print(line.decode().strip())