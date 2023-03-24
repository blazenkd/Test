/*
Data Types 
C supports the following basic data types: 

int: integer, a whole number.

float: floating point, a number with a fractional part.

double: double-precision floating point value.

char: single character.

The amount of storage required for each of these types varies by platform. 

C has a built-in sizeof operator that gives the memory requirements for a particular data type.

For example:
The program output displays the corresponding size in bytes for each data type.

The printf statements in this program have two arguments. 
The first is the output string with a format specifier (%ld), 
while the next argument returns the sizeof value. In the final output, 
the %ld (for long decimal) is replaced by the value in the second argument.
*/

#include <stdio.h>

int main() 
{
    printf("int: %ld \n", sizeof(int));
    printf("float: %ld \n", sizeof(float));
    printf("double: %ld \n", sizeof(double));
    printf("char: %ld \n", sizeof(char));

    return 0;
}

/*
Note that C does not have a boolean type.

A printf statement can have multiple format specifiers with corresponding arguments 
to replace the specifiers. Format specifiers are also referred to as conversion 
specifiers.

We will learn more about format specifiers in the upcoming lessons.
*/

