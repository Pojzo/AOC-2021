const ROW_BITS = 12;

fs = require('fs');
fs.readFile('input', 'utf8', function (err, data) {
    if (err) {
        return console.log(err);
    }
    handleData(data);
});

function calculateOxygen(data) {
    let zeros; 
    let ones;
    let most_common;
    let i = 0;
    while (data.length != 1 && i < data[0].length) {
        zeros = ones = 0;
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == '1') {
                ones += 1;
            }
            else {
                zeros += 1;
            }
        }
        if (ones >= zeros) {
            most_common = '1';
        }
        else {
            most_common = '0';
        }
        new_array = []
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == most_common) {
                new_array.push(data[j]);
            }
        }
        data = copyArray(new_array);
        i += 1;
    }
    return data[0];
}

function calculateCarbon(data) {
    let zeros; 
    let ones;
    let most_common;
    let i = 0;
    let new_array;
    while (data.length != 1) {
        zeros = ones = 0;
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == '1') {
                ones += 1;
            }
            else {
                zeros += 1;
            }
        }
        if (zeros <= ones) {
            most_common = '0'
        }
        else {
            most_common = '1';
        }
        new_array = [];
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == most_common) {
                new_array.push(data[j]);
            }
        }
        data = copyArray(new_array);
        i += 1;
    }
    return data[0];
}

function copyArray(array) {
    new_array = []
    for (let i = 0; i < array.length; i++) {
        new_array[i] = array[i];
    }
    return new_array;
}

function handleData(data) {
    data = data.split('\n');
    let data2 = copyArray(data);
    let oxygen = calculateOxygen(data);
    let carbon = calculateCarbon(data2);
    let oxygen_length = oxygen.length;
    let carbon_length = carbon.length;
    let oxygen_value = 0;
    let carbon_value = 0;
    for (let i = 0; i < oxygen_length; i++) {
        if (oxygen[i] == '1') {
            oxygen_value += Math.pow(2, oxygen_length - 1 - i);
        }
    }

    for (let i = 0; i < carbon_length; i++) {
        if (carbon[i] == '1') {
            carbon_value += Math.pow(2, carbon_length - 1 - i);
        }
    }
    console.log(oxygen, carbon);
    console.log(oxygen_value, carbon_value);
    console.log(oxygen_value * carbon_value);
}
