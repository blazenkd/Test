/*
Functions are central to C programming and are used to accomplish
a program solution as a series of subtasks. 

By now you know that every C program contains a main() function.
And you're familiar with the printf() function. 

You can also create your own functions. 

A function:

 • is a block of code that performs a specific task

 • is reusable

 • makes a program easier to test

 • can be modified without changing the calling program

Even a simple program is easier to understand when main() is broken down into subtasks that are implemented with functions. 

For example, it's clear that the goal of this program is to calculate the square of a number: 
*/

#include <stdio.h>

/*
In order to use the square function, we need to declare it.

Declarations usually appear above the main() function and take the form:

return_type function_name(parameters);
*/

int square(int num) {
  return num * num;
}

/*
A function is not required to return a value, but a return type must
still be in the declaration. In this case, the keyword void is used.

For example, the display_message function declaration indicates the
function does not return a value: void display_message();

When the parameter types and names are included in a declaration,
the declaration is called a function prototype.

For example, the square function prototype appears above main(): 

#include <stdio.h>

// declaration 
int square (int num); 

int main() {
  int x, result;
  
  x = 5;
  result = square(x);
  printf("%d squared is %d\n", x, result);
    
  return 0;
}

Our square function returns an integer and takes one parameter of type int.

The last step is actually defining the function.
Function definitions usually appear after the main() function.

The complete program below shows the square function declaration and definition:

A function's parameters are used to receive values required by the function.
Values are passed to these parameters as arguments through the function call. 

By default, arguments are passed by value, which means that a copy of data
is given to the parameters of the called function. The actual variable isn't
passed into the function, so it won't change.

Arguments passed to a function are matched to parameters by position.
Therefore, the first argument is passed to the first parameter, the
second to the second parameter, and so on.

The following program demonstrates parameters passed by value:
*/

int sum_up (int x, int y); 

int main_2() {
    int x, y, result;
  
    x = 3;
    y = 12;
    result = sum_up(x, y);
    printf("%d + %d = %d", x, y, result);
    
    return 0;
}

int sum_up (int x, int y) { 
    x += y;
    return(x);
} 

/*
Variable scope refers to the visibility of variables within a program. 

Variables declared in a function are local to that block of code
and cannot be referred to outside the function. 

Variables declared outside all functions are global to the entire program. 

For example, constants declared with a #define at the top of a program are
visible to the entire program.

The following program uses both local and global variables: 
*/

int global1 = 0; 

int main_3() {    
    int local1, local2;
  
    local1 = 5;
    local2 = 10;
    global1 = local1 + local2;
    printf("%d \n", global1);  /* 15 */
    
    return 0;
}

/*
Static variables have a local scope but are not destroyed when a function is exited.
Therefore, a static variable retains its value for the life of the program and can
be accessed every time the function is re-entered.

A static variable is initialized when declared and requires the prefix static.

The following program uses a static variable: 
*/

void say_hello();

int main_4() {	
    int i;

    for (i = 0; i < 5; i++) {
        say_hello();
    }
   
    return 0;
}

void say_hello() {
    static int num_calls = 1;

    printf("Hello number %d\n", num_calls);
    num_calls++;
}


int main() {
  int x, result;
  
  x = 5;
  result = square(x);
  printf("%d squared is %d\n", x, result);
    
  main_2();
  printf("\n");
  main_3();
  main_4();
  return 0;
}
