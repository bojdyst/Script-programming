const textField = document.forms[0].elements[0];
const numberField = document.forms[0].elements[1];
const button = document.forms[0].elements[2];

function onClickHandler() {
    window.alert("Text field: " + textField.value + " --> " + typeof(textField.value) + 
    "\nNumber field: " + numberField.value + " --> " + typeof(numberField)); 
}        

button.onclick = onClickHandler;