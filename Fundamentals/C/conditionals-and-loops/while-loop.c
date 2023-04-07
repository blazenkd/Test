/*
The while statement is called a loop structure because it executes statements repeatedly
while an expression is true, looping over and over again. It takes the form: 

while (expression) {
  statements
}

The expression evaluates to either true or false, and statements can be a single statement or,
more commonly, a code block enclosed by curly braces { }.

For example:

The code below will output the count variable 7 times.
The while loop evaluates a condition before the loop is entered,
making it possible that the while statements never execute.

An infinite loop is one that continues indefinitely because the loop
condition never evaluates to false. This may cause a run-time error.

Run the code and see how it works!
*/

#include <stdio.h>

int count() {
  int count = 1;
  
  while (count < 8) {
    printf("Count = %d\n", count);
    count++;
  }
    
  return 0;
}

/*
The do-while Loop 
The do-while loop executes the loop statements before evaluating the
expression to determine if the loop should be repeated. 

It takes the form: 

do {
  statements
} while (expression);

The expression evaluates to either true or false, and statements can be
a single statement or a code block enclosed by curly braces { }.

For example:

*/

// Run main function
int main() {
    count();
    return 0;
}