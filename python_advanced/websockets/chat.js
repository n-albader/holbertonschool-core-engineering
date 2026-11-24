
const socket = new WebSocket("ws://localhost:8000/ws");

const status = document.getElementById("status");
const messages = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");

function displayMessage(sender, message) {
    const messageElement = document.createElement("div");

    messageElement.classList.add("message");
    messageElement.textContent = `${sender}: ${message}`;

    messages.appendChild(messageElement);

    messages.scrollTop = messages.scrollHeight;
}

// Connection established
socket.onopen = () => {
    status.textContent = "Connected";
    status.style.color = "green";
};

// Receive messages from the server
socket.onmessage = (event) => {
    displayMessage("Server", event.data);
};

// Connection closed
socket.onclose = () => {
    status.textContent = "Disconnected";
    status.style.color = "red";
};

// Connection error
socket.onerror = () => {
    status.textContent = "Connection error";
    status.style.color = "red";
};

// Send messages
form.addEventListener("submit", (event) => {
    event.preventDefault();

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    if (socket.readyState === WebSocket.OPEN) {
        socket.send(message);

        displayMessage("You", message);

        input.value = "";
        input.focus();
    }
});