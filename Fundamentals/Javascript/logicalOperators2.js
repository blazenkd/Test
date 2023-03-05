/*  
We've seen that the AND operator requires all conditions to be true. But what if it's enough for only one
condition to be true?

For example, the light bulb here switches on if the battery is connected or the power is connected.

For such conditions, we use the OR operator ||, which returns true as long as at least one of the conditions is true.
*/

let isBatteryOn = true;
let isPowerOn = false;

console.log(isBatteryOn || isPowerOn);

// If all the conditions are false, then the || operatur returns false. Set the isPowerOn variable to false.
isBatteryOn = false;
console.log(isBatteryOn || isPowerOn);

// We know that the NOT operator ! negates a boolean value. That means that it returns true if a condition is false
// and vice versa.

let isBulbOn = true;
console.log(!isBulbOn);

// We can use ! to negate logical expressions as well. To do that, we place the logical expression between 
// parentheses.
isBatteryOn = true;
isPowerOn = false;
console.log(!(isBatteryOn && isPowerOn));

// The logical expression returns false but by negating it, we get true.
console.log(isBatteryOn && isPowerOn);
console.log(!(isBatteryOn && isPowerOn));

// Which logical operator returns true if at least one of the conditions is true?
// ||

// What does this code display in the console?
const condition1 = 5 > 6;
const condtiion2 = 9 ===10;
console.log(condition1 || condtiion2);

// Which operator do we use to reverse the outcome of a logical expression?
// !

// Which of the following code snippets negates the logical expression?
// !(condition1 && condition2)

// What does this code display in the console?
let condition3 = true;
let condition4 = false;
const logicalExpression = condition3 || condition4;
console.log(!logicalExpression || logicalExpression);

// Check if a person can buy a car depending on whether their loan is approved or their cash amount is greater than
// the car cost?
let isLoanApproved = true;
let cash = 30000;
let cost = 40000;
const isCarBought = isLoanApproved || (cash > cost);
console.log(isCarBought);

// Save the opposite of isLoanRejected into the variable
let isLoanRejected = false;
const isLoanGranted = !isLoanRejected;
console.log(isLoanGranted);

// Check if a person can buy a car or not.
let loanRejected = false;
const insufficientFunds = cash < cost;
const canBuyCar = !(loanRejected && insufficientFunds);
console.log(canBuyCar);

// Use the || and ! operators to determine if a user can post, by checking if any attachment is added or if the text
// field is not empty.
let isTextEmpty = true;
let isAttachment = false;
const isPosted = isAttachment || !isTextEmpty;
console.log(isPosted);

// Save a file if the cloud storage is greater than the file size or the system storage is greater than the file size.
let cloudStorage = 4;
let systemStorage = 8;
let fileSize = 5;
const result = (cloudStorage > fileSize) || (systemStorage > fileSize);
console.log("Saved? : " + result)