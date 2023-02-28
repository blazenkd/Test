// Checking Number Equality

/* 
We learned how to create and store values but how do we compare them?
We need to compare numbers in situations like checking a user's entered PIN matches their
saved PIN.
*/

const enteredPIN = 5448;
const expectedPIN = 5448;

/*
To compare if two numbers are the same, we use the equality operator, ===
*/

5===5

// When comparing, there are only two results: true or false

/*
When we compare the same numbers with the equality operator, the result is true.
*/

console.log(10===10);

/* 
When we compare two different numbers with the equality operator, the result is false.
*/

console.log(9===10);

// What do we use to check if two numbers are equal?
// ===

// What does this code display in the console?
console.log(10 === 11);


// In which of these situations would we need to check if two numbers are equal?
// When checking if user's level is 10

// What does this code display in the console?
console.log(5+13);
console.log(5===13);

// Check if the value of votes is equal to 11
const votes = 10;
console.log(votes === 11);

// Add the equality comparison operator.
console.log(99===100);

// Display false in the console.
console.log(10 === 13);

// Check if these numbers are the same by typing ===
console.log(100===100);

// To check if a number isn't equal to another number, we use the inequality operator !==
console.log(1 !== 100);

// We can store the result of a comparison with the inequality operator in a variable.
// Save the comparison between 1 and 2 into the variable result.
const result = 1 !== 2;
console.log(result);

// Variables can store the result of equality comparisons, too.
const result_1 = 1 === 2;
console.log(result_1);

// We can compare values with variables and variables with other variables.
// Type === to compare the contents of the variables.
const one = 1;
const two = 2;
console.log(one === two);
console.log(one !== two);

// Which value should batteryLevel have, so that the comparison in the charged variable gives false?
const batteryLevel = 78;
const charged = batteryLevel === 100;

// What does this code display in the console?
const result_2 = 7 !== 10;
console.log(result_2);

// What value should we give to the variable emails to store true in inboxFull?
const emails = 1000;
const inboxFull = emails === 1000;

// What should the value of scoreOne be if we want equal to be true?
const scoreOne = 80;
const scoreTwo = 80;
const equal = scoreOne === scoreTwo;

// Add the operator that makes the comparison false.
console.log(10 !== 10);

// Check if answer equals 13 and store the result in correctAnswer.
const answer = 16;
const correctAnswer = answer === 13;
console.log(correctAnswer);

// Check if the user's current level equal highestLevel by typing ===
const level = 5;
const highestLevel = 50;
console.log(level === highestLevel);

// Check if the answer submitted by the user isn't empty by typing !==
const letters = 12;
const validAnswer = letters !== 0;