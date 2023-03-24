/*
Input 

C supports a number of ways for taking user input.
getchar() Returns the value of the next single character input. 
*/


// #include <stdio.h>

// int main() 
// {
//   char a = getchar();

//   printf("You entered: %c", a);

//   return 0;
// }


/*
The input is stored in the variable a.

The gets() function is used to read input as an ordered sequence of characters, 
also called a string.
A string is stored in a char array.

For example:
*/


// #include <stdio.h>

// int main() 

// {
//   char a[100];

//   gets(a); 

//   printf("You entered: %s", a);

//   return 0;
// }


/*
Here we stored the input in an array of 100 characters.
scanf() scans input that matches format specifiers.

For example:
*/


// #include <stdio.h>

// int main() {
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

int main() {
  int a, b;
  printf("Enter two numbers:");
  scanf("%d %d", &a, &b);

  printf("\nSum: %d", a+b);

  return 0;
}

/*
scanf() stops reading as soon as it encounters a space, 
so text such as "Hello World" is two separate inputs for scanf().
*/
