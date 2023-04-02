'use strict';
//Football betting app
//Web data below
const game = {
    team1: 'Bayern Munich',
    team2: 'Borrussia Dortmund',
    players: [
    ['Neuer','Pavard','Martinez','Alaba','Davies','Kimmich','Goretzka','Coman','Muller','Gnarby','Lewandowski',],
    ['Burki','Schulz','Hummels','Akanji','Hakimi','Weigl','Witsel','Hazard','Brandt',
    'Sancho','Gotze',],
    ],
    
    score: '4:0',
    scored: ['Lewandowski', 'Gnarby', 'Lewandowski','Hummels'],
    date: 'Nov 9th, 2037',
    odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
    },};
//Personal code here

let players1 = new Array();//This is output as a single string, need to change it so each element is counted individually (maybe a while/for loop?)(is there a non-loop method?)
for (let i=0; i < game.players[0].length; i++) {
    let playerAppend = game.players[0][i]; 
    // console.log(`PLAYERS 1 OUTPUT: ${players1}`)
    players1.push(playerAppend);
} 
// console.log(players1)
// console.log(typeof players1)

const players2 = new Array(game.players[1]);
//Tasks for Bayern Munich
const gk = players1[0];
const fieldPlayers = players1;
fieldPlayers.shift();
const allPlayers = new Array();//array where u append player1 and player2  

const players1Final = [...players1]
players1Final.push('Thiago','Coutinho','Perisic')

let team1 = game.odds.team1;
let draw = game.odds.x; 
let team2 = game.odds.team2;

const printGoals = (names) => {//takes in values, increments count to track   goals scored
    let count = 0;
    while (count < names.length){
        console.log(names[count]);
        count += 1;
        console.log(`Goals scored: ${count}`);
    };
    
    // console.log(`Total goals: ${score}`) //Unreachable
}
printGoals(game.scored)


//TASK 7 - INCOMPLETE, Watch vid to check
switch (game.odds) {
    case game.odds == team1: console.log(`Team 2 wins`) 
    break;
    case game.odds == team2: console.log(`Team 1 wins`)
    break;
    default: `Default case`
}


// console.log(players1Final)
// console.log(typeof players1Final)
// console.log(players1)

// console.log(allPlayers)
// console.log(typeof allPlayers)
// console.log(`Players1: ${players1}`)
// console.log(fieldPlayers)