function startAction() {
    let result = document.getElementById("result");
    result.setAttribute("placeholder", "");
    let error_message = document.getElementById("error_message");
    if (error_message) {
        error_message.remove();
    }
}

function writeInBar(input) {
    startAction();
    let result = document.getElementById("result");
    let prevValue = result.getAttribute("value");
    result.setAttribute("value", prevValue + input);
}

function undo() {
    startAction();
    let result = document.getElementById("result");
    let prevValue = result.getAttribute("value");
    let newValue = prevValue.slice(0, -1);
    result.setAttribute("value", newValue);
}

function clearBar() {
    startAction();
    let result = document.getElementById("result");
    result.setAttribute("value", "");
}