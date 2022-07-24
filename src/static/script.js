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

function run () {
    const code = document.getElementById('code-text').innerText;
    const resultEl = document.getElementById('output')
    const fn = new Function(code)
    resultEl.innerHTML = fn()
}

codeInput.registerTemplate("syntax-highlighted", codeInput.templates.prism(Prism, []));