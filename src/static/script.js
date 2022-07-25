document.getElementById("year").innerText = new Date().getFullYear();

var client_name = prompt("What is your name?");
document.querySelector("#ws-id").textContent = client_name;
var ws = new WebSocket(`ws://localhost:8000/ws/${client_name}`);
ws.onmessage = function (event) {
    var messages = document.getElementById("messages");
    messages.value += event.data + '\n';
};
function sendMessage(event) {
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

let pyodideReadyPromise = main();

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

codeInput.registerTemplate("syntax-highlighted", codeInput.templates.prism(Prism, []));