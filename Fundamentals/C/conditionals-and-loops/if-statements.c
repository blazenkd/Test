/*
Nested if Statements 
An if statement can include another if statement to form a nested statement.
Nesting an if allows a decision to be based on further requirements. 

Appropriately indenting nested statements will help clarify the meaning to a reader. 
However, be sure to understand that an else clause is associated with the closest if 
unless curly braces { } are used to change the association.

For example:

Consider the following statement: 

*/

#include <stdio.h>

int bonus_1() {
    int profit = 1400;
    int clients = 18;
    int bonus;
    
    if (profit > 1000){
        if (clients > 15)
            bonus = 100;
        else
            bonus = 25;
    }
    printf("%d\n", bonus);
}

int bonus_2() {
    int profit = 500;
    int clients = 12;
    int bonus = 0;
    
    if (profit > 1000) {
        if (clients > 15)
            bonus = 100;
    }
    else
        bonus = 25;
    
    printf("%d\n", bonus);
}

/*
When a decision among three or more actions is needed, the if-else if statement can be used.

There can be multiple else if clauses and the last else clause is optional.

For example:
*/

int grade() {
    int score = 89;
  
    if (score >= 90)
        printf("%s", "Top 10% \n");
    else if (score >= 80)
        printf("%s", "Top 20% \n");
    else if (score > 75)
        printf("%s", "You passed.\n");
    else
        printf("%s", "You did not pass.\n");
}

// Run the functions
int main() {
    bonus_1();
    bonus_2();
    grade();
    return 0;
}