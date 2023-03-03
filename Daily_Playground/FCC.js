/* 
Just as we can build a string over multiple lines out of string literals, we can also append variables to a 
string using the plus equals (+=) operator.
Example: 
*/

const anAdjective = "awesome!";
let ourStr = "freeCodeCamp is ";
ourStr += anAdjective;
console.log(ourStr);

// Set someAdjective to a string of at least 3 characters and append it to myStr using the += operator.
// Change code below this line
const someAdjective = "Fun";
let myStr = "Learning to code is ";
myStr += someAdjective;
console.log(myStr);