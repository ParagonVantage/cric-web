const chatbox = document.getElementById('chatbox');
const messageInput = document.getElementById('message');
const sendButton = document.getElementById('send');

async function sendMessage() {
  const message = messageInput.value.trim();
  if (!message) return;
  chatbox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
  messageInput.value = '';
  try {
    const response = await fetch('/api/financial-chatbot', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
  } catch (err) {
    chatbox.innerHTML += `<p><strong>Error:</strong> Unable to get response.</p>`;
  }
  chatbox.scrollTop = chatbox.scrollHeight;
}

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    sendMessage();
  }
});
