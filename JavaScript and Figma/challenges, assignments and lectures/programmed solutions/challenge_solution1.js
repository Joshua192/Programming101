const heightMark = 1.88;
const heightJohn = 1.76;
const massMark = 95;
const massJohn = 85;

const markBMI = massMark / heightMark ** 2;
const johnBMI = massJohn / heightJohn ** 2;

console.log("Mark BMI:",markBMI,"\nJohn's BMI:", johnBMI);

const markHigherBMI = markBMI > johnBMI;
console.log(markHigherBMI);