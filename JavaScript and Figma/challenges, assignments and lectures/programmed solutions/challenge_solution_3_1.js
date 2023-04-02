const forecastTemp = [17,21,23] //Data set 1
// forecastTemp = [12,5,-5,0,4] //Data set 2
printForecast = (temperatureArray) => {
    let outputStr = '';
    for (x = 0;x<temperatureArray.length;x++) {
        let dayTemp =temperatureArray[x];
        let countdown = x+1;
        outputStr = outputStr + `Good morning, the temperature will be ${dayTemp} in ${countdown} days. . . `;
        }
        console.log(' Finished!\n\n\n')
        console.log(outputStr)

}
printForecast(forecastTemp)