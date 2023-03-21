/*

A variable is a name for an area in memory.

The name of a variable (also called the identifier) must begin with either a letter 
or an underscore and can be composed of letters, digits, and the underscore character. 

Variable naming conventions differ, however using lowercase letters with an underscore 
to separate words is common (snake_case). 

Variables must also be declared as a data type before they are used.

The value for a declared variable is changed with an assignment statement. 

For example, the following statements declare an integer variable my_var and then 
assigns it the value 42: 
*/

// int my_var;
// my_var = 42;

/*
You can also declare and initialize (assign an initial value) a variable 
in a single statement:
*/

// #int my_var = 42;

/*
As you can see, you can declare multiple variables on a single line by 
separating them with a comma. Also, notice the use of format specifiers for 
float (%f) and char (%c) output.
*/

#include <stdio.h>

int main() {
  int a, b;
  float salary = 56.23;
  char letter = 'Z';
  a = 8;
  b = 34;
  int c = a+b;

  printf("%d \n", c);
  printf("%f \n", salary);
  printf("%c \n", letter);

  return 0;
}

/*
The C programming language is case-sensitive, so my_Variable and my_variable 
are two different identifiers.
*/