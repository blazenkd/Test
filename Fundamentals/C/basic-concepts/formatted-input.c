/*
Formatted Input 
The scanf() function is used to assign input to variables. 
A call to this function scans input according to format specifiers that convert input as necessary. 
If input can't be converted, then the assignment isn't made.
The scanf() statement waits for input and then makes assignments: 
*/

// #include <stdio.h>

// int main() {
//     int x;
//     float num;
//     char text[20];
//     scanf("%d %f %s", &x, &num, text);
// }

/*
Typing 10 22.5 abcd and then pressing Enter assigns 10 to x, 22.5 to num, and abcd to text.

Note that the & must be used to access the variable addresses. 
The & isn't needed for a string because a string name acts as a pointer.

Format specifiers begin with a percent sign % and are used to assign values to 
corresponding arguments after the control string. Blanks, tabs, and newlines are ignored.

A format specifier can include several options along with a conversion character:

%[*][max_field]conversion character

The optional * will skip the input field.

The optional max_width gives the maximum number of characters to assign to an input field.

The conversion character converts the argument, if necessary, to the indicated type:

d decimal

c character

s string

f float

x hexadecimal

For example:
*/

#include <stdio.h>

int main() {
    int x, y;
    char text[20];

    scanf("%2d %d %*f %5s", &x, &y, text);
    /* input: 1234  5.7  elephant */
    printf("%d  %d  %s", x, y, text);
    /* output: 12  34  eleph */

    return 0;
} 