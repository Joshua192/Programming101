
const heightMark = 1.69;
const heightJohn = 1.95;
const massMark = 78;
const massJohn = 92;

let markBMI = massMark / heightMark ** 2;
let johnBMI = massJohn / heightJohn ** 2;

// console.log("Mark BMI:",markBMI,"\nJohn's BMI:", johnBMI);

markBMI = Math.round(markBMI*10)/10;
johnBMI = Math.round(johnBMI*10)/10;
// console.log(markBMI);

const markHigherBMI = markBMI > johnBMI;

if (markHigherBMI){
    console.log(`Mark's BMI (${markBMI}) is higher than John's!(${johnBMI})!`);} else{
        console.log(`John's BMI (${johnBMI}) is higher than Mark's!(${markBMI})!`);
    }