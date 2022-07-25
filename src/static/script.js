//The Functions
function sendMessage(event, ws) {
    var input = document.getElementById("messageText");
    ws.send(input.value);
    input.value = "";
    event.preventDefault();
}

async function main() {
    let pyodide = await loadPyodide();
    console.log("Ready!\n");
    return pyodide;
}

const show = (Id) => {
    document.getElementById(Id).style.display = "block";
}

const hide = (Id) => {
    document.getElementById(Id).style.display = "none";
}

var pyodideReadyPromise = main();

const run = async () => {
    let code = document.getElementById("code-text").value;
    let pyodide = await pyodideReadyPromise;
    try {
        pyodide.runPython(code);
        show("success-alert");
    } catch (err) {
        console.log(err);
        show('warning-alert');
    }
}
// End Functions
// The things that happen when the page loads
document.getElementById("year").innerText = new Date().getFullYear();

var client_name = prompt("What is your name?");
document.querySelector("#ws-id").textContent = client_name;
var ws = new WebSocket(`ws://localhost:8000/ws/${client_name}`);
ws.onmessage = function (event) {
    var messages = document.getElementById("messages");
    messages.value += event.data + '\n';
};

codeInput.registerTemplate("syntax-highlighted", codeInput.templates.prism(Prism, []));

document.getElementById("messageText").onkeyup = function(e){
    e = e || Event;
    if (e.key === "enter" && !e.ctrlKey) {
        sendMessage(e);
    };
    return true;
}
// End of the function of the page load.