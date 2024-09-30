const socket = new WebSocket('ws://localhost:5000');

socket.onmessage = (event) => {
    console.log(`Received message: ${event.data}`);
    const messageList = document.getElementById('message-list');
    const messageElement = document.createElement('li');
    messageElement.textContent = event.data;
    messageList.appendChild(messageElement);
};

socket.onopen = () => {
    console.log('Connected to the server');
};

socket.onerror = (event) => {
    console.log(`Error occurred: ${event}`);
};

socket.onclose = () => {
    console.log('Disconnected from the server');
};

document.getElementById('send-button').addEventListener('click', () => {
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value;
    socket.send(message);
    messageInput.value = '';
});

//renderizar a lista de contatos
const renderContactList = (contacts) => {
    const contactList = document.getElementById('contact-list');
    contactList.innerHTML = '';
    contacts.forEach((contact) => {
        const contactElement = document.createElement('li');
        contactElement.textContent = contact.name;
        contactList.appendChild(contactElement);
    });
};

//mensagens
const renderMessageList = (messages) => {
    const messageList = document.getElementById('message-list');
    messageList.innerHTML = '';
    messages.forEach((message) => {
        const messageElement = document.createElement('li');
        messageElement.textContent = message.text;
        messageList.appendChild(messageElement);
    });
};

//equisição para obter a lista de contatos
fetch('/contacts')
    .then(response => response.json())
    .then(contacts => renderContactList(contacts));

// mensagens
fetch('/messages')
    .then(response => response.json())
    .then(messages => renderMessage.List(messages));