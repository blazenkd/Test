# 2/18/2023
# ---ChatGPT---
'''
"Why do we import random?"
    We import the random module to generate random values or to make random choices. 

    In the provided example code, the random module is used to select a random symbol from the list of 
    symbols for each column in the slot machine spin.

What are the attributes (methods and properties) of the random module?
    
    # print(dir(random))
    
'''
import random

'''
What are capitalized variables used for?

    # They are typically used as constants.
    # They are used to define values that will not be changed during the execution of the program.
    # This is a convention followed by Python programmers to indicate that the value of the variable
    should not be changed. Although Python does not enforce constants, it is considered good practice
    to use capitalized letters for constant values.
'''

ROWS = 1
COLS = 3

'''How do we generate a dictionary for our slot machine?'''

symbol_count = {
    "A" : 3,
    "B" : 6,
    "C" : 9,
    "D" : 12
}


'''How do we create a function that gets our slot machine spin based on rows, cols, and symbols?'''
def get_slot_machine_spin(rows, cols, symbols):
    '''Why do we start by creating an all_symbols list?'''
    all_symbols = []
    '''How do we check our progress with print?'''
    print(all_symbols)
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    print(all_symbols)


    columns = []
    print(range(cols))
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        print("Current Symbols: ", current_symbols)
        for _ in range(rows):
            value = random.choice(current_symbols)
            print("Value: ", value)
            current_symbols.remove(value)
            print("Current Symbols_updated: ", current_symbols)
            column.append(value)
            print("Column:", column)
        columns.append(column)
        print("Column Appending: ", columns)
    return columns


spin = get_slot_machine_spin(ROWS, COLS, symbol_count)
print(spin)
'''Practice'''


