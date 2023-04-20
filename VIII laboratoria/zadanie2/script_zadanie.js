"use strict"

let total = 0;

function cyfry(input) {
    let sum = 0;

    for (let i = 0; i < input.length; i++) { 
        if (!isNaN(String(input[i]) * 1)) //string*1 == NaN number*1 == number
            sum += parseInt(input[i]);
    }

    return sum;
}

function litery(input) {
    let quantity = 0;

    for (let i = 0; i < input.length; i++) {
        if((input[i] >= 'A' && input[i] <= 'Z') ||
             (input[i] >= 'a' && input[i] <= 'z'))
                quantity += 1;
    }

    return quantity;
}

function suma(input) {
    let number = parseInt(input);

    if (!isNaN(number)) {
        total += number;
    }
    
    return total;
}