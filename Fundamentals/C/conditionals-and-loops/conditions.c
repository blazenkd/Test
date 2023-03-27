/*
Conditionals are used to perform different computations or actions 
depending on whether a condition evaluates to true or false.


The if Statement 

The if statement is called a conditional control structure because it
executes statements when an expression is true. For this reason, the 
if is also known as a decision structure. It takes the form: 

if (expression)
  statements

The expression evaluates to either true or false, and statements can be 
a single statement or a code block enclosed by curly braces { }.

For example:
In the code above we check whether the score variable is greater than 75, 
and print a message if the condition is true.
*/

#include <stdio.h>

int pass() {
  int score = 89;
  
  if (score > 75)
    printf("You passed.\n");
    
  return 0;
}

/*
Relational Operators 
There are six relational operators that can be used
to form a Boolean expression, which returns true or false:

    <    less than

    <=  less than or equal to

    >    greater than

    >=  greater than or equal to

    ==  equal to

    !=   not equal to

*/

int add_one() {
    int num = 41;
    num += 1;
    if (num == 42) {
        printf("You won!\n");
    }
}

/*
An expression that evaluates to a non-zero value is considered true.
For example:
*/

int stock() {
    int in_stock = 20;
    if (in_stock)
        printf("Order received.\n"); 
}

/*
The if-else Statement 
The if statement can include an optional else clause that executes statements
when an expression is false.

For example, the following program evaluates the expression and then executes
the else clause statement:
*/

int grade_A() {
    int score = 89;
  
    if (score >= 90)
        printf("Top 10%%.\n");
    else
        printf("Less than 90.\n");
    
    return 0;
}


/*
Conditional Expressions 
Another way to form an if-else statement is by using the ?: operator in a
conditional expression. The ?: operator can have only one statement 
associated with the if and the else.

This is equivalent to:
  if (x >= 5)
    y = 5;
  else
    y = x;

For example:
*/

int check() {
    int y;
    int x = 3;

    y = (x >= 5) ?  5 : x;

    printf("%d", y);

    return 0;
}

// Run the functions
int main() {
  pass();
  add_one();
  stock();
  grade_A();
  check();
  return 0;
}
