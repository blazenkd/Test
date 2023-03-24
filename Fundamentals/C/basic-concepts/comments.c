/*
Comments 

Comments are explanatory information that you can include in a program to benefit the reader of your code. 
The compiler ignores comments, so they have no affect on a program.

A comment starts with a slash asterisk and ends with an asterisk slash and can be anywhere in your code. 

Comments can be on the same line as a statement, or they can span several lines.

For example:
*/


// #include <stdio.h>

// /* A simple C program
//  *  Version 1.0
//  */
// int main() {
//     /* Output a string */
//     printf("Hello World!");
//     return 0;
// }


/*
As you can see, comments clarify the program's intent to the reader. 
Use comments to clarify the purpose and logic behind segments of code.
*/

/*
C++ introduced a double slash comment // as a way to comment single lines. 
Some C compilers also support this comment style.

For example:
*/

#include <stdio.h>

int main() {
  int x = 42; //int for a whole number
    
  //%d is replaced by x
  printf("%d", x);
    
  return 0;
}

/*
Adding comments to your code is good programming practice. 
It facilitates a clear understanding of the code for you and for others who read it.
*/