# 2/12/2023
# ---FreeCodeCamp---

import re
import random
import string

def generate_word(word_length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(word_length))

def join_word_with_symbol(word, symbol):
    return f"{word}{symbol}"

word_length = int(input("Enter word length: "))
symbol = '@'
word = generate_word(word_length)
data = join_word_with_symbol(word, symbol) + join_word_with_symbol(word, symbol) + " " + join_word_with_symbol(word, symbol)
print(data)

atpos = data.find('@')
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

