// commands:
// kowalski buy camaro
// kowalski rent camaro
// kowalski return camaro

var button = document.getElementById("button1");
var textarea = document.getElementById("textarea1");
var operations = "";
var tmp = []
var listOfOperations = [];
var dealerWarehouse = {}; //{model: [brand, sell price, rent price, quantity, url]}
var dealerClients = {}; //{name: {car: price, amount, rent start date, rent end date}}

dealerWarehouse["mustang"] = ["ford", "150000", "10000", "3", "Programowanie Skryptowe\\VIII laboratoria\na lekcji\\mustang.jpg"];
dealerWarehouse["camaro"] = ["chevrolet", "180000" , "12000", "2", "Programowanie Skryptowe\\VIII laboratoria\\na lekcji\\camaro.jpg"];
dealerWarehouse["charger"] = ["dodge", "200000", , "14000", "4", "Programowanie Skryptowe\\VIII laboratoria\\na lekcji\\charger.jpeg"];
dealerWarehouse["challenger"] = ["dodge", "250000" , "18000", "1", "Programowanie Skryptowe\\VIII laboratoria\\na lekcji\\challenger.jpg"];
dealerWarehouse["stinger"] = ["kia", "100000", "8000", "3", "Programowanie Skryptowe\\VIII laboratoria\\na lekcji\\stinger.jpg"];

function emptyTextAreaWhenClick() {
    textarea.value = "";
}

function getDataAfterClickingButton() {
    console.log("Data has been got and will be processed in a while");
    operations += textarea.value;
    tmp = operations.split('\n');

    for(var i = 0; i < tmp.length; i++) {
        listOfOperations.push(tmp[i].split(' '));
    }

    // window.alert(listOfOperations);

    // window.alert(operations);
    // window.alert(listOfOperations);
    // console.log(operations);

    for(var i = 0; i < listOfOperations.length; i++) {
        if (listOfOperations[i][1] == "buy") {
            buyCar(listOfOperations[i][2], listOfOperations[i][0]);
        } 
        else if (listOfOperations[i][1] == "rent") {
            rentCar(listOfOperations[i][2], listOfOperations[i][0]);
        } 
        else if (listOfOperations[i][1] == "return") {
            returnCar(listOfOperations[i][2], listOfOperations[i][0]);
        } 
        else if (listOfOperations[i][0] == "warehouse") {
            showWarehouse();
        } 
        else if (listOfOperations[i][0] == "summary") {
            summary();
        } 
    } 
}

function buyCar(carName, buyerName) {
    if (dealerWarehouse[carName][3] > 0) {
    if (buyerName in dealerClients){
        if (carName in dealerClients[buyerName]) {
            dealerClients[buyerName][carName][1] = parseInt(dealerClients[buyerName][carName][1]) + 1;
            dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) - 1;
        } else {
            dealerClients[buyerName][carName] = [dealerWarehouse[carName][1], 1, "", ""];
            dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) - 1;
        }
    } else {
        dealerClients[buyerName] = {};
        dealerClients[buyerName][carName] = [dealerWarehouse[carName][1], 1, "", ""];
        dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) - 1;
    }

    // dealerClients[buyerName] = [carName, dealerWarehouse[carName][1]];

    // if (parseInt(dealerWarehouse[carName][3]) - 1 < 0) {
    //     dealerClients[buyerName][carName][1] = parseInt(dealerClients[buyerName][carName][1]) - 1;
      
    // } else {
    //     dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) - 1;
    // }

    // for (const [key, value] of Object.entries(dealerClients)) {
    //     window.alert(key + ":" + value);
    // }
} else {
    window.alert("Cannot procedure operation on that car! Out of stock!");
}
}

function rentCar(carName, buyerName) {
    if (buyerName in dealerClients){
        if (carName in dealerClients[buyerName])
            window.alert("Cannot rent a car when You've already bought it!")
    } else {
        if (parseInt(dealerWarehouse[carName][3]) - 1 < 0) {
            window.alert("Cannot procedure operation on that car! Out of stock!")
        } else {
            dealerClients[buyerName] = {};
            dealerClients[buyerName][carName] = [dealerWarehouse[carName][2], 1, new Date().toJSON().slice(0,10).replace(/-/g,'/'), ""];
            dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) - 1;
        }
    }


    // for (const [key, value] of Object.entries(dealerClients)) {
    //     window.alert(key + ":" + value);
    // }
}

function returnCar(carName, buyerName) {
    if (carName in dealerClients[buyerName]) {
        if ((dealerClients[buyerName][2]) !== "") {
            dealerClients[buyerName][carName] = [dealerWarehouse[carName][2], 0, new Date().toJSON().slice(0,10).replace(/-/g,'/'), new Date().toJSON().slice(0,10).replace(/-/g,'/')];
            dealerWarehouse[carName][3] = parseInt(dealerWarehouse[carName][3]) + 1;
        } else {
            window.alert("You have to previously rent a car to be able to return it!");
    } 
    } else {
        window.alert("You have to previously rent a car to be able to return it!");
    }

    // for (const [key, value] of Object.entries(dealerClients)) {
    //     window.alert(key + ":" + value);
    // }
}

function showWarehouse() {
    for (const [key, value] of Object.entries(dealerWarehouse)) {
        window.alert(key + ":" + value);
    }
}

function summary() {
    for (const [key1, value1] of Object.entries(dealerClients)) {
        for (const [key, value] of Object.entries(value1)) {
            window.alert(key1 + ": " + key + ":" + value);
        }
    }
}

button.onclick = getDataAfterClickingButton;
textarea.onclick = emptyTextAreaWhenClick;