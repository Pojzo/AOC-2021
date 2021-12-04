const ROW_BITS = 12;

fs = require('fs');
fs.readFile('input', 'utf8', function (err, data) {
    if (err) {
        return console.log(err);
    }
    handleData(data);
});

function calculateGammaRate(data) {
    let zeros; 
    let ones;
    let final_arr;
    let gamma_rate = 0;
    for (let i = 0; i < ROW_BITS; i++) {
        zeros = ones = 0;
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == '1') {
                ones += 1;
            }
            else {
                zeros += 1;
            }
        }
        if (ones > zeros) {
            gamma_rate += Math.pow(2, ROW_BITS - i - 1);
        }
    }
    return gamma_rate;
}

function calculateEpsilonRate(data) {
    let zeros; 
    let ones;
    let final_arr;
    let epsilon_rate = 0;
    for (let i = 0; i < ROW_BITS; i++) {
        zeros = ones = 0;
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == '1') {
                ones += 1;
            }
            else {
                zeros += 1;
            }
        }
        if (ones < zeros) {
            epsilon_rate += Math.pow(2, ROW_BITS - i - 1);
        }
    }
    return epsilon_rate;

}

function handleData(data) {
    var data = data.split('\n');
    var gamma_rate  = calculateGammaRate(data);
    var epsilon_rate  = calculateEpsilonRate(data);
    console.log(gamma_rate * epsilon_rate);
}
