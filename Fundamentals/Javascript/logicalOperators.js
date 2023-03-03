/*
With logical operators, we can connect two or more conditions to decie a result.
Turn on the light bulb by cnnecting both the switch and battery.

A logical operator connects the two conditions for the battery and switch to decide if the bulb must
be turned on or off.

The AND operator && returns true only if all the conditions are true.
*/
let isBatteryOn = true;
let isSwitchOn = true;
console.log(isBatteryOn && isSwitchOn);

/* 
The && operater will return false if one or more conditions are false. In the code, assign false to the
isSwitchOn variable.
*/

isSwitchOn = false;
console.log(isBatteryOn && isSwitchOn);

/*
When operands and operators compute a boolean value together, it forms a logical expressions, like
isBatteryOn && isSwitchOn
*/
isBatteryOn = false;
console.log(isBatteryOn && isSwitchOn);

/*
You can also store the result of a logical expression in a variable.
*/
let result = isBatteryOn && isSwitchOn;
console.log(result);

// Which logical operator gives us true if al the conditions are true?
// &&

// What does this code print in the console?
let condtion1 = false;
let condition2 = true;
let result1 = condtion1 && condition2;
console.log(result1)

// Which of the following is a logical expression?
// condition1 && condition2

// What does this code display in the console?
let cost = 50;
let sellPrice = 60;
const profit = sellPrice - cost;
const result2 = cost < sellPrice && profit > 0;
console.log(result2);

/* Check if a license can be issued to a person. Their age should be 18 or more and they should
pass the driving test.
*/

let age = 18;
let isPass = true;
const isEligible = age >= 18 && isPass;
console.log(isEligible);

/* Check if the user can send an e-mail. For that, the recipient should be valid and the subject should
be filled.
*/

let isRecipientValid = true;
let isSubjectFilled = false;
const isMailSent = isRecipientValid && isSubjectFilled;
console.log("Mail Sending Successful?: " + isMailSent);

// Store the logical expression in a const variable.

isRecipientValid = true;
isSubjectFilled = false;
const result3 = isRecipientValid && isSubjectFilled;
console.log(result3)

/* Store a logical expression in the willSiteLoad variable that checks if the WiFi is connected and the URL
is valid to load a website.
*/

let isWifiConnected = true;
let isURLValid = true;
const willSiteLoad = isWifiConnected && isURLValid;
console.log(willSiteLoad);