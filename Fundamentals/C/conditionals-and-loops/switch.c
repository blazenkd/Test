/*
The switch Statement 
The switch statement branches program control by matching the result of an 
expression with a constant case value. 

The switch statement often provides a more elegant solution to if-else if 
and nested if statements.

The switch takes the form: 
*/

#include <stdio.h>

int value() {
    int num = 3;

    switch (num) {
        case 1:
            printf("One\n");
            break; 
        case 2:
            printf("Two\n");
            break; 
        case 3:
            printf("Three\n");
            break; 
        default:
            printf("Not 1, 2, or 3.\n");
    }
}

/*
The switch Statement 
There can be multiple cases with unique labels.

The optional default case is executed when no other matches are made.

A break statement is needed in each case to branch to the end of the switch statement.

Without the break statement, program execution falls through to the next case statement. 
This can be useful when the same statement is needed for several cases. 
Consider the following switch statement: 
*/

int breaks() {
    int num = 3;

    switch (num) {
        case 1:
        case 2:
        case 3:
            printf("One, Two, or Three.\n");
            break;   
        case 4:
        case 5:
        case 6:
            printf("Four, Five, or Six.\n");
            break;
        default:
            printf("Greater than Six.\n");
    }  
}

int main() {
    value();
    breaks();
    return 0;
}