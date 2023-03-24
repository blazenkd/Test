/*
Arithmetic Operators: 
 
C supports arithmetic operators + (addition), - (subtraction), * (multiplication), / (division), 
and % (modulus division). 

Operators are often used to form a numeric expression such as 10 + 5, 
which in this case contains two operands and the addition operator. 

Numeric expressions are often used in assignment statements.
For example:
*/

#include <stdio.h>

int calculate_area() {
  int length = 10;
  int width = 5;
  int area;

  area = length * width;
  printf("%d \n", area);  /* 50 */

  return 0;
}


/*
Division:

C has two division operators: / and %.

The division / operator performs differently depending on the data types of the operands. 
When both operands are int data types, integer division, also called truncated division, 
removes any remainder to result in an integer. When one or both operands are real numbers (float or double), 
the result is a real number.

The % operator returns only the remainder of integer division. It is useful for many algorithms, 
including retrieving digits from a number. Modulus division cannot be performed on floats or doubles.

The following example demonstrates division:
*/


int calculate_division() {
    int i1 = 10;
    int i2 = 3;
    int quotient, remainder;
    float f1 = 4.2;
    float f2 = 2.5;
    float result;

    quotient = i1 / i2;  // 3
    remainder = i1 % i2;  // 1
    result = f1 / f2;  // 1.68

    printf("%d \n", quotient);
    printf("%d \n", remainder);
    printf("%f \n", result);

    return 0;
}

/*
Operator Precedence:

C evaluates a numeric expression based on operator precedence. 

The + and – are equal in precedence, as are *, /, and %. 

The *, /, and % are performed first in order from left to right and then + and -, also in order from left to right.

You can change the order of operations by using parentheses ( ) to indicate which operations are to be performed first. 

For example, the result of 5 + 3 * 2 is 11, where the result of (5 + 3) * 2 is 16.
*/

int calculate_operator_precedence() {
    int a = 6;
    int b = 4;
    int c = 2;
    int result;
    result = a - b + c;  // 4
    printf("a - b + c = %d \n", result);
    result = a + b / c;  // 8
    printf("a + b / c = %d \n", result);
    result = (a + b) / c;  // 5
    printf("(a + b) / c = %d \n", result);

    return 0;
}

/*
Type Conversion:

When a numeric expression contains operands of different data types, 
they are automatically converted as necessary in a process called type conversion.

For example, in an operation involving both floats and ints, 
the compiler will convert the int values to float values.

In the following program, the increase variable is automatically converted to a float: 
*/

int calculate_type_conversion() {
  float price = 6.50;
  int increase = 2;
  float new_price;

  new_price = price + increase;
  printf("New price is %4.2f\n", new_price);
  /* Output: New price is 8.50 */

  return 0;
}

/*
Note the format specifier includes 4.2 to indicate the float is to be printed in a space at 
least 4 characters wide with 2 decimal places.

When you want to force the result of an expression to a different type you can perform explicit 
type conversion by type casting, as in the statements:

Without the type casting, average will be assigned 5.

Explicit type conversion, even when the compiler may do automatic type conversion, 
is considered good programming style.
*/

int calculate_type_casting() {
    float average;
    int total = 23;
    int count = 4;

    average = (float) total / count;
    /* average = 5.75 */
    printf("The average is: %.2f\n", average);
    return 0;
}

/*
Assignment Operators 
An assignment statement evaluates the expression on the right side of the equal sign first and then 
assigns that value to the variable on the left side of the =. This makes it possible to use the same 
variable on both sides of an assignment statement, which is frequently done in programming.

For example:
*/

int calculate_assignment_operators() {
    int x = 2;

    x += 1;  // 3
    x -= 1;  // 2
    x *= 3;  // 6
    x /= 2;  // 3
    x %= 2;  // 1
    x += 3 * 2;  // 7
    printf("x is: %d\n", x);
    return 0;
}

/*
Increment & Decrement 
Adding 1 to a variable can be done with the increment operator ++. Similarly, the decrement operator -- 
is used to subtract 1 from a variable.

The prefix form increments/decrements the variable and then uses it in the assignment statement.
The postfix form uses the value of the variable first, before incrementing/decrementing it.

For example:
*/


void calculate_increment_decrement() {
    int x, y, z;

    z = 3;
    z--;  /* decrement z by 1 */
    y = 3;
    y++; /* increment y by 1 */
    x = z--;  /* assign 2 to x, then decrement z to 1 */
    x = ++y;  /* increment y to 5, then assign 5 to x */

    printf("Final values: x = %d, y = %d, z = %d\n", x, y, z);
}


int main() {
  calculate_area();
  calculate_division();
  calculate_operator_precedence();
  calculate_type_conversion();
  calculate_type_casting();
  calculate_assignment_operators();
  calculate_increment_decrement();
  return 0;
}