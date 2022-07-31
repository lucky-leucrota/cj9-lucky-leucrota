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
};

const hide = (Id) => {
  document.getElementById(Id).style.display = "none";
};

var pyodideReadyPromise = main();

const run = async () => {
  let code = document.getElementById("code-text").value;
  let pyodide = await pyodideReadyPromise;
  try {
    pyodide.runPython(code);
    show("success-alert");
  } catch (err) {
    console.log(err);
    show("warning-alert");
  }
};
// End Functions
// The things that happen when the page loads
document.getElementById("year").innerText = new Date().getFullYear();

var client_name = prompt("What is your name?");
document.querySelector("#ws-id").textContent = client_name;

// uncomment below line to deploy to heroku
// var ws = new WebSocket(`wss://${window.location.host}/ws/${client_name}`);
// uncomment below line to tun on localhost
var ws = new WebSocket(`ws://${window.location.host}/ws/${client_name}`);

ws.onmessage = function (event) {
  // var messages = document.getElementById("messages");
  // messages.value += event.data + '\n';
  messagesContainer = document.getElementById("messages-container");
  var chatBubble = document.createElement("div");
  chatBubble.className = "chat-bubble";
  let join_leave_message_check = (event) => {
    let arr = event.data.split(" ");
    if (arr[1] === "joined") {
      let card = document.getElementById("users");
      let user = document.createElement("p");
      user.classList.add("card-text");
      user.id = arr[0];
      user.textContent = arr[0];
      card.appendChild(user);
    } else if (arr[1] == "left") {
      let user = document.getElementById(arr[0]);
      user.remove();
    } else {
      return;
    }
  };
  join_leave_message_check(event);
  var chatName = document.createElement("span");
  chatName.textContent = event.data.split(":", 2)[0];
  var chatMessage = document.createElement("p");
  chatMessage.textContent = event.data.split(":", 2)[1];

  messagesContainer.appendChild(chatBubble);
  chatBubble.appendChild(chatName);
  chatBubble.appendChild(chatMessage);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
  document.getElementById("count").innerText =
    document.getElementById("users").childElementCount;
  // messagesContainer.innerHTML += event.data + '\n';
};

codeInput.registerTemplate(
  "syntax-highlighted",
  codeInput.templates.prism(Prism, [])
);
// End of the function of the page load.