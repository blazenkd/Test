/*
Logical operators && and || are used to form a compound Boolean expression that
tests multiple conditions. A third logical operator is ! used to reverse the
state of a Boolean expression.

The && Operator  

The logical AND operator && returns a true result only when both expressions are true.

For example:

The statement above joins just two expressions, but logical operators can be used to join
multiple expressions.

A compound Boolean expression is evaluated from left to right. Evaluation stops when no further
test is needed for determining the result, so be sure to consider the arrangement of operands
when one result affects the outcome of a later result.
*/

#include <stdio.h>

int and_operator() {
    int n = 42;

    if (n > 0 && n <= 100)
        printf("Range (1 - 100).\n");
}

/*
The || Operator 
The logical OR operator || returns a true result when any one expression or both expressions are true. 

Parentheses are used for clarity even though && has higher precedence than || and will be evaluated first.

For example:
*/

int or_operator() {
    char n = 'X';

    if (n == 'x' || n == 'X')
        printf("Roman numeral value 10.\n");
}

int or_operator_2() {
    int n = 42;
    
    if (n == 999 || (n > 0 && n <= 100))
        printf("Input valid.\n");
}

/*
The ! Operator 
The logical NOT operator ! returns the reverse of its value. 

NOT true returns false, and NOT false returns true.

In C, any non-zero value is considered true and a 0 is false.
The logical NOT operator therefore, converts a true value to 0 and a false value to 1.
*/

int reverse() {
    char n = 'V';
    
    if (!(n == 'x' || n == 'X'))
        printf("Roman numeral is not 10.\n");
}

// Problem

int problem(){
    int x = 3;

    int y = 8;

    if(!(x > 2 || y < 0)) 

        printf("true");

    else 

        printf("false");
}

int main() {
    and_operator();
    or_operator();
    or_operator_2();
    reverse();
    problem();
    return 0;
}