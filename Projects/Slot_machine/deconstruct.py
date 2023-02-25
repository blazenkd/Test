import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 6,
    "C" : 9,
    "D" : 12
}

'''
The function takes three arguments rows, cols, and symbols. rows and cols determine the dimensions of 
the slot machine, while symbols is a dictionary that maps the symbols to their counts.
'''
def get_slot_machine_spin(rows, cols, symbols):
    '''
    The all_symbols list is created by iterating over the symbols dictionary and adding symbol_count 
    copies of each symbol to the all_symbols list.
    '''
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    '''
    A list of cols columns is created, and for each column, a list of rows symbols is generated.
    '''
    columns = []
    for _ in range(cols):
        column = []
        '''
        current_symbols is a copy of the all_symbols list. 
        '''
        current_symbols = all_symbols[:]
        '''
        In each iteration of the inner loop, a 
        random symbol is chosen from current_symbols using the random.choice() function. The chosen 
        symbol is then removed from current_symbols using the list.remove() method to ensure that it 
        can't be chosen again in the same column. The chosen symbol is then appended to the current 
        column.
        '''
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        '''
        Once all rows symbols have been generated for a column, the column is appended to the list 
        of columns.
        '''
        columns.append(column)

    '''
    Finally, the function returns the list of columns.
    '''
    print("Get Slot Machine Spin", columns)
    return columns


'''
This function print_slot_machine takes a list of columns as input and prints it as a slot machine grid.
'''
def print_slot_machine(columns):
    '''
    The function iterates through the rows of the grid using a for loop with range(len(columns[0])), 
    which goes from 0 to the number of rows in the grid (assuming all columns have the same number of 
    rows).
    '''
    for row in range(len(columns[0])):
        '''
        For each row, the function iterates through the columns of the grid using a for loop with 
        enumerate(columns).
        '''
        for i, column in enumerate(columns):
            '''
            For each column, the function prints the symbol at the current row using 
            print(column[row], end = " | "), separated by a pipe symbol (|) from the symbols in 
            the next column.
            '''
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            
            else:
                print(column[row], end = "")
            '''
            When it reaches the last column, the function prints the symbol at the current row 
            without the pipe symbol using print(column[row], end = "").
            '''
        '''
        Finally, the function prints a newline character using print(), which moves the printing 
        cursor to the next row.
        '''
        print()
    
slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
print_slot_machine(slots)  


