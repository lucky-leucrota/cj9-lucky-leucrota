var ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = function (event) {
    var messages = document.getElementById("texta");
    //var message = document.createElement('li')
    //var content = document.createTextNode(event.data)
    //message.appendChild(content)
    //messages.appendChild(message)
    messages.value += "Received:" + event.data + "\n";
};
    
function sendt() {
    var v = document.getElementById("texta");
    var msg = document.getElementById("msg").value;
    ws.send(msg);
    var msg = "Sent:" + msg + "\n";
    v.value += msg;
}

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}