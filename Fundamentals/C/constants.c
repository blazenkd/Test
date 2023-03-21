/*
A constant stores a value that cannot be changed from its initial assignment. 
By using constants with meaningful names, code is easier to read and understand. 
To distinguish constants from variables, a common practice is to use uppercase 
identifiers.
One way to define a constant is by using the const keyword in a variable declaration: 
*/

#include <stdio.h>

// int main() {
//   const double PI = 3.14;
//   printf("%f", PI);
    
//   return 0;
// }


/*
The value of PI cannot be changed during program execution.
For example, another assignment statement, such as PI = 3.141 will generate an error.
Another way to define a constant is with the #define preprocessor directive.
The #define directive uses macros for defining constant values.
For example:
*/

#define PI 3.14

int main() {
  printf("%f", PI);
  return 0;
}
/*
Before compilation, the preprocessor replaces every macro identifier in the code with 
its corresponding value from the directive. In this case, every occurrence of PI is 
replaced with 3.14.

The final code sent to the compiler will already have the constant values in place.

The difference between const and #define is that the former uses memory for storage 
and the latter does not.

Do NOT put a semicolon character at the end of #define statements. 
This is a common mistake.

We will learn more about preprocessor directives in the next modules.
*/
