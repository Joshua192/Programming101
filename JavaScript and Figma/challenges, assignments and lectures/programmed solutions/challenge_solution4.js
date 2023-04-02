//15% tip if bill between 50-300
//20% tip otherwise

let bill_vaule = 430;
let tip;
50 <= bill_vaule <= 300 ? tip=0.15*bill_vaule : tip=0.2*bill_vaule;
console.log(`Your bill is: ${bill_vaule}\nYour tip is: ${tip}\n Your final total comes to: ${bill_vaule+tip}`) 