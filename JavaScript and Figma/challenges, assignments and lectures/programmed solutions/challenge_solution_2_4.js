let bills = [ 22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
let tips = [];
let total = [];
let average;

let tip = 0;
const calcTip = (bill_vaule) => {//Takes in bill, calculates tip based on pre-req criteria. returns tip.
    50 <= bill_vaule <= 300 ? tip=0.15*bill_vaule : tip=0.2*bill_vaule;
    console.log(`Your bill is: ${bill_vaule}\nYour tip is: ${tip}\n Your final total comes to: ${bill_vaule+tip}`) 
    return tip; 
}

let tipArr = [];
for (let i = 0; i<bills.length; i++){
    store = calcTip(bills[i])
    console.log(`Your stored bill value: ${store}`)
    tipArr.push(store)
    console.log(`The tipArr array: [${tipArr}]`)
    totalVar = bills[i] + tipArr[i]
    total.push(totalVar)
    console.log(`Total array = [${total}]`)    
}

const calcAverage = (arrIn) =>{
    let sums=0;
    let count;
    for (let i = 0; i < arrIn.length; i++) {
        sums += arrIn[i];
        count = i
        console.log(`sums equal to: ${sums}`)
        console.log(`count is: ${i}`)
    }
    console.log(`Final sum: ${sums}`)
    average = sums/count;
    console.log(`The average bill is: $${average}`)
    return average;
}
calcAverage(bills);