/*
The for Loop 
The for statement is a loop structure that executes statements a fixed number of times. 

It takes the form: 

    for (initvalue; condition; increment) {
    statements;
    }

The initvalue is a counter set to an initial value. This part of the for loop is performed only once.

The condition is a Boolean expression that compares the counter to a value before each loop iteration,
stopping the loop when false is returned.

The increment increases (or decreases) the counter by a set value.

For example, the program below displays 0 through 9:
*/

#include <stdio.h>

int single_digit() {
    int i;
    int max = 10;
  
    for (i = 0; i < max; i++) {
        printf("%d\n", i);
    }
}

/*

The for loop can contain multiple expressions separated by commas in each part. 

For example:

    for (x = 0, y = num; x < y; i++, y--) { 
    statements; 
    }

Also, you can skip the initvalue, condition and/or increment.

For example:
*/

int func() {
    int i=0;
    int max = 10;
  
    for (;i < max; i++) {
        printf("%d\n", i);
    }
}

/*
Loops can also be nested.

When writing a program this way, there is an outer loop and an inner loop.
For each iteration of the outer loop the inner loop repeats its entire cycle.

In the following example, nested for loops are used to output a multiplication table:
*/

int func_2() {
    int i, j;
    int table = 10;
    int max = 12;
  
    for (i = 1; i <= table; i++) {
        for (j=0; j <= max; j++) {
            printf("%d x %d = %d\n", i, j, i*j);
        }
        printf("\n"); /* blank line between tables */
    }
    
    return 0;
}

/*
A break in an inner loop exits that loop and execution continues with the outer loop.

A continue statement works similarly in nested loops.
*/

int main() {
    single_digit();
    func();
    func_2();
    return 0;
}