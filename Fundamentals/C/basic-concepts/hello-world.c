/*
As when learning any new language, the place to start is with the classic "Hello World!" program: 

Let's break down the code to understand each line:

#include <stdio.h> The function used for generating output is defined in stdio.h. 
In order to use the printf function, we need to first include the required file, 
also called a header file.

int main() The main() function is the entry point to a program. 
Curly brackets { } indicate the beginning and end of a function (also called a code block). 
The statements inside the brackets determine what the function does when executed.

The printf function is used to generate output: 

Here, we pass the text "Hello World!" to it.

The \n escape sequence outputs a newline character. 
Escape sequences always begin with a backslash \.

The semicolon ; indicates the end of the statement. 
Each statement must end with a semicolon.

return 0; This statement terminates the main() function and returns the value 0 to the calling process. 
The number 0 generally means that our program has successfully executed. 
Any other number indicates that the program has failed.
*/

#include <stdio.h>

int main() 
{
    printf("Hello, World!\n");
    printf("Hi, everyone!\n");
    return 0;
}