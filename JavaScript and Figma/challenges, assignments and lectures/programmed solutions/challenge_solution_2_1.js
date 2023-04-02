const calcAverage = (score1, score2, score3) => (score1+score2+score3)/3;

const dolphins = calcAverage(44,23,71);
const koalas = calcAverage(65,54,49);
const dolphins2 = calcAverage(85,54,41);
const koalas2 = calcAverage(23,34,27);

function checkWinner(avgDolphins, avgKoalas) {
    if (avgDolphins >= 2*avgKoalas) {
    return `Dolphins win! (${avgDolphins} vs. ${avgKoalas}).`;
    }   else if (avgKoalas >= 2*avgDolphins) {
    return `Koalas win! (${avgKoalas} vs. ${avgDolphins}).`;
    } else {`Neither has won!`;}
}


console.log(checkWinner(dolphins,koalas))
console.log(checkWinner(dolphins2,koalas2))