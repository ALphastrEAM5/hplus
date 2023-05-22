document.addEventListener("DOMContentLoaded", () => {
    const chatbox = document.querySelector(".chatbox");
    const chatboxButton = document.querySelector(".chatbox__button button");
    const chatboxSupport = document.querySelector(".chatbox__support");
    const chatboxMessages = document.querySelector(".chatbox__messages");
    const chatboxFooter = document.querySelector(".chatbox__footer");
    const messageInput = document.querySelector(".chatbox__footer input");
    const sendButton = document.querySelector(".chatbox__send--footer");
  
    chatboxButton.addEventListener("click", () => {
      chatboxSupport.classList.toggle("chatbox--active");
    });
  
    sendButton.addEventListener("click", () => {
      const message = messageInput.value.trim();
      if (message !== "") {
        appendMessage(message, "visitor");
        sendMessage(message);
        messageInput.value = "";
      }
    });
  
    messageInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        sendButton.click();
      }
    });
  
    function appendMessage(message, sender) {
        const messageItem = document.createElement("div");
        messageItem.classList.add("messages__item");
        messageItem.classList.add(`messages__item--${sender}`);
        messageItem.innerText = message;
        
        // Insert the message item as the first child of chatboxMessages
        if (chatboxMessages.firstChild) {
          chatboxMessages.insertBefore(messageItem, chatboxMessages.firstChild);
        } else {
          chatboxMessages.appendChild(messageItem);
        }
        
        chatboxMessages.scrollTop = chatboxMessages.scrollHeight;
      }
      
  
    function sendMessage(message) {
      const xhr = new XMLHttpRequest();
      xhr.open("POST", "/predict", true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText).answer;
            appendMessage(response, "operator");
          } else {
            console.error("Request failed. Status:", xhr.status);
          }
        }
      };
      const data = JSON.stringify({ message });
      xhr.send(data);
    }
  });
  