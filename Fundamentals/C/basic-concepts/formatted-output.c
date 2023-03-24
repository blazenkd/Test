/*
Formatting Output 

The printf function was introduced in your very first Hello World program. 
A call to this function requires a format string which can include escape sequences for outputting 
special characters and format specifiers that are replaced by values.
*/


// #include <stdio.h>

// int main() {
//     printf("The tree has %d apples.\n", 22);
//     /* output: The tree has 22 apples. */

//     printf("\"Hello World!\"\n");
//     /* output: "Hello World!" */
// }


/*
Escape sequences begin with a backslash \:

\n new line

\t horizontal tab

\\ backslash

\b backspace

\' single quote

\" double quote

Format specifiers begin with a percent sign % and are replaced by corresponding arguments 
after the format string. A format specifier can include several options along with a conversion character:

The optional - specifies left alignment of the data in the string.

The optional width gives the minimum number of characters for the data.

The period . separates the width from the precision.

The optional precision gives the number of decimal places for numeric data. If s is used as the conversion character, then precision determines the number of characters to print.

The conversion character converts the argument, if necessary, to the indicated type:

d decimal

c character

s string

f float

e scientific notation

x hexadecimal

*/


#include <stdio.h>

int main() {
    printf("Color: %s, Number: %d, float: %5.2f \n", "red", 42, 3.14159);
    /* Color: red, Number: 42, float:  3.14  */

    printf("Pi = %3.2f \n", 3.14159); 
    /* Pi = 3.14 */
    
    printf("Pi = %8.5f \n", 3.14159); 
    /* Pi = 3.14159 */
    
    printf("Pi = %-8.5f \n", 3.14159); 
    /* Pi = 3.14159 */
    
    printf("There are %d %s in the tree. \n", 22, "apples");
    /* There are 22 apples in the tree. */
}