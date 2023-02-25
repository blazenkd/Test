'''
Inputs
'''
import random

ROWS = 4
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 6,
    "C" : 9,
    "D" : 12
}

def get_spin(rows, cols, symbols):
    all_symbols = []

    for key, value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)
            print(all_symbols)

    columns = []

    for i in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for i in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

print("\nReturn", get_spin(ROWS, COLS, symbol_count))