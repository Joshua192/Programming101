let tip = 0;
const calcTip = (bill_vaule) => {//Takes in bill, calculates tip based on pre-req criteria. returns
    50 <= bill_vaule <= 300 ? tip=0.15*bill_vaule : tip=0.2*bill_vaule;
    console.log(`Your bill is: ${bill_vaule}\nYour tip is: ${tip}\n Your final total comes to: ${bill_vaule+tip}`) 
    return tip; 
}
// calcTip(500)

const bills = new Array(235,555,44)
const tipArr = []
const total = []

for (let i = 0; i<bills.length; i++){
    store = calcTip(bills[i])
    console.log(`Your stored bill value: ${store}`)
    tipArr.push(store)
    console.log(`The tipArr array: [${tipArr}]`)
    totalVar = bills[i] + tipArr[i]
    total.push(totalVar)
    console.log(`Total array = [${total}]`)    
}