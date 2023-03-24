'''
CS50 Python 2023
Week 1: extensions.py
'''

'''
Task :

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs
that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

    # .gif
    # .jpg
    # .jpeg
    # .png
    # .pdf
    # .txt
    # .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
which is a common default.
'''

import os
import mimetypes

# Define a dictionary to map file extensions to media types
media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Get input from user and strip any leading/trailing whitespace
filename = input("File name: ").strip()

# Use os.path.splitext() to split the filename into a tuple containing the base name and extension,
# and select the last element (the file extension) with [-1]. Use lower() to convert the extension to lowercase.
file_ext = os.path.splitext(filename)[-1].lower()


# Look up the media type in the dictionary, or default to application/octet-stream
media_type = media_types.get(file_ext, "application/octet-stream")

# Output the result
print(media_type)