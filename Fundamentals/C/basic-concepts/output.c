/*
Output 
We have already used the printf() function to generate output in the previous lessons. 
In this lesson, we cover several other functions that can be used for output.

putchar() Outputs a single character.
*/


// #include <stdio.h>

// int main() {
//   char a = getchar();

//   printf("You entered: ");
//   putchar(a);

//   return 0;
// }


/*
The input is stored in the variable a.
The puts() function is used to display output as a string.
A string is stored in a char array.

For example:
*/


// #include <stdio.h>

// int main() {
//   char a[100];

//   gets(a); 

//   printf("You entered: ");
//   puts(a); 

//   return 0;
// }


/*
Here we stored the input in an array of 100 characters.
scanf() scans input that matches format specifiers.

For example:
*/


// #include <stdio.h>

// int main() 
// {
//   int a;
//   scanf("%d", &a);

//   printf("You entered: %d", a);

//   return 0;
// }


/*
The & sign before the variable name is the address operator. 
It gives the address, or location in memory, of a variable. 
This is needed because scanf places an input value at a variable address

As another example, let's prompt for two integer inputs and output their sum:
*/


#include <stdio.h>

int main() 
{
  int a, b;
  printf("Enter two numbers:");
  scanf("%d %d", &a, &b);

  printf("\nSum: %d", a+b);

  return 0;
}