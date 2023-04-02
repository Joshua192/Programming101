'use strict';
let thisYear = new Date().getFullYear();
// console.log('176'+54);
// false && console.log(67+(+'176'))
// let a;
// a && console.log(a);

// function introduction(){
    //     return 'My name is Josh.';
    // }
    // console.log(introduction());
    
    // function fruitProcess(apple,orange){
    //         console.log(`Pressing ${apple} apples and ${orange} oranges...\nDone!`);
    //     }
    //     fruitProcess(5,3);
        
        // function calcAge1(birthYear){//takes current year and calculates age based on arguement given by user
        //     let thisYear = new Date().getFullYear()
        //     return `You are ~${thisYear - birthYear} years old!\n`;
// }

// const calcAge2 = function (birthYear){//functionally the same but this is called an anonymous function
//     let thisYear = new Date().getFullYear()
//     return `You are ~${thisYear - birthYear} years old!\n`;
// }

// const age1 = calcAge1(2003);
// const age2 = calcAge2(2000);
// console.log(age1, age2);

//This is an arrow function, it's very quick to write and works very well for writing simple one line functions. It implicitly returns whatever is written so no need to write the word return.
// const calcAge3 = birthYear => `You are ~${thisYear - birthYear} years old!\n`;
// console.log(calcAge3(1987))

// const retireCondensed = birthYear => `You have ${65-thisYear+birthYear} years until retirement!`;

// const yearsUntilRetire = (birthYear, firstName) => {//If you have a multi-line function you utilise 'return' and curly braces as normal.
//     const age = thisYear - birthYear;
//     const retirement = 65 - age;
//     return `${firstName} has ${65-thisYear+birthYear} years until retirement!`;
// }

// console.log(yearsUntilRetire(1998,"Barbara"))

// Function calling another Function!
// const fruitCut = function (fruit) {
//     return fruit *4;
// }

// const fruitProcess = function (apple,orange){
//     const applePieces = fruitCut(apple);
//     const orangePieces = fruitCut(orange);
//     console.log(`Juicing ${applePieces} apple pieces and ${orangePieces} orange pieces...\nDone!`);
// }
// fruitProcess(5,3);

// (() => {
//     console.log("Automatic Singularly Self-executing Anonymous Function (ASS AF)");
// })
// ();
   
// Arrays
// const years = new Array();//Alternate way to create arrays

// let friends = [['Micheal Brandenburg',23],['Amy Hoffman',35],['Carl Jung',78],['Kyle Rainer',45],['Haime Reyes', 19]];
// console.log(`Picking an element in an array is straightforward: ${friends[1]}`);
// console.log(friends)
// console.log(`This is the last element in the array: [${friends[friends.length-1]}]`);

// friends[2] = ["Carl Jung",13];
// console.log(friends);

// const returnArray = (arrIn) => {//tried to create a loop to print every element in an array/list. It works for both.
//     let i = 0;
//     while (i < arrIn.length, i++) {
//         console.log(arrIn[i]);
//         console.log(`I is equal to ${i}`);
//     }
// }
// returnArray(friends);

// const subtract19 = (arrIn) => {
//     console.log(`This section has been reached`)
//     const age = 19;

//     for (let x = 0; x<arrIn.length; x++) {// Trying to create program that loops through each array element and subtracts 19(arbitrary no).
//         console.log(`For loop accessed`);
//         console.log(`Array before operation: ${arrIn}\n`)
//         console.log(`Value of array at x before operation: ${arrIn[x]}\n`)
//         arrIn[x] = arrIn[x] - age;
//         console.log(`Value of array at x after operation: ${arrIn[x]}`)
//         console.log(`This is x: ${x}`)
//     }    
//     console.log(`This is outside the loop`)
//     console.log(`Array post-op: [${arrIn}]`)
// }
// const yearArray = [1997,2001,2003,1988,1979];
// subtract19(yearArray);

//New function subtracting one arrays value from another.
//Can add another bit where it works up to the size of the smaller array. DID THAT EZ

const arraySub = (arrayOne, arrayTwo) => {
    console.log(`Array One: [${arrayOne}]\nArray Two: [${arrayTwo}]`)
    let shorterArr = []
    let largerArr = []
    if (arrayTwo.length < arrayOne.length){
        shorterArr = arrayTwo
        largerArr = arrayOne
        console.log(`Array Two has been assigned as the shorter arr`)
    } else {
        shorterArr = arrayOne;
        largerArr = arrayTwo;
    }
    //I could make it more complex with another if statement and a var that stores the larger arr and only subtracts 
    //  from the chosen/larger of the two. would need a largerArr and otherArr var tho. Cumbersome. DID THAT based on the length of the arrays, no user input needed.

    let endpoint = 0;
    console.log(`This is going to do two things:\n 1) array One - array Two\n 2)array Two - array One.`)
    for (let x = 0; x<shorterArr.length;x++) {
        arrayOne[x] = arrayOne[x] - arrayTwo[x];
        console.log(`Array one updated value ${x}: ${arrayOne[x]}`);
        // arrayTwo[x] = arrayTwo[x] - arrayOne[x]
        // console.log(`Array two updated value ${x}: ${arrayTwo[x]}`)    
        endpoint = x;
    }
    largerArr[endpoint] = largerArr[endpoint] + `}`;//Appends curly brace to the end of array where shorter array runs out.
    console.log(`For loop has been exited.`)
    console.log(`Post-op output: Array One:[${arrayOne}].\nArray Two: [${arrayTwo}].`)

}

arraySub([35,31,67,89,34,99,104],[24,45,67,33,12])