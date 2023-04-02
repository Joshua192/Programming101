const averageDolphins = 123;
const averageKoalas = 153;

console.log(` Dolphins average: ${averageDolphins}`);
console.log(`Koalas average: ${averageKoalas}`);

doplphinWinner = averageDolphins > averageKoalas;
if (doplphinWinner && averageDolphins>=100) {
    console.log(`Dolphins are the winners!`);
} else if (averageDolphins === averageKoalas && averageKoalas >= 100) {
    console.log(`Dolphins and Koalas draw!`);
} else if (averageKoalas > averageDolphins && averageKoalas > 100)console.log(`Koalas are the winners!`);
else console.log(`Neither team wins :(`)

// Average score calculation
//compare scores, higher average wins -> above 100
//Draws can happen -> scores > 100, score1 == score2