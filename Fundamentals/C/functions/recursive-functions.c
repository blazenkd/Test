/*
Recursive Functions 
An algorithm for solving a problem may be best
implemented using a process called recursion.
Consider the factorial of a number, which is commonly written as 5! = 5 * 4 * 3 * 2 * 1. 

This calculation can also be thought of as repeatedly calculating num * (num -1) until num is 1.

A recursive function is one that calls itself and includes a base case,
or exit condition, for ending the recursive calls. In the case of computing a factorial,
the base case is num equal to 1.

For example: 

*/

#include <stdio.h>

//function declaration
int factorial(int num);

int main() {    
  int x = 5;

  printf("The factorial of %d is %d\n", x, factorial(x));
 
  return 0;
}

//function definition
int factorial(int num) {
  
  if (num == 1)  /* base case */
    return (1);
  else
    return (num * factorial(num - 1));
} 

/*
The program output is: The factorial of 5 is 120

Recursion works by "stacking" calls until the base case is executed.
At that point, the calls are completed from newest to oldest.
The factorial call stack can be thought of as:

2*factorial(1)

3*factorial(2)

4*factorial(3)

5*factorial(4)

When the base case is reached, the return value 1 triggers the
completion of the stacked calls. The return values from newest
to oldest creates the following calculations, with the final
calculation (5 * 24) being returned to the calling function main():

2 * 1

3 * 2

4 * 6

5 * 24

*/

