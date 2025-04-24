document.addEventListener("DOMContentLoaded", function () {
  const chatbotButton = document.createElement("button");
  chatbotButton.innerText = "Chat with us!";
  chatbotButton.style.position = "fixed";
  chatbotButton.style.bottom = "20px";
  chatbotButton.style.right = "20px";
  chatbotButton.style.backgroundColor = "#007bff";
  chatbotButton.style.color = "#fff";
  chatbotButton.style.border = "none";
  chatbotButton.style.padding = "10px 15px";
  chatbotButton.style.borderRadius = "5px";
  chatbotButton.style.cursor = "pointer";
  document.body.appendChild(chatbotButton);

  const chatbotPopup = document.createElement("div");
  chatbotPopup.style.position = "fixed";
  chatbotPopup.style.bottom = "70px";
  chatbotPopup.style.right = "20px";
  chatbotPopup.style.width = "300px";
  chatbotPopup.style.height = "400px";
  chatbotPopup.style.backgroundColor = "#fff";
  chatbotPopup.style.border = "1px solid #ccc";
  chatbotPopup.style.borderRadius = "5px";
  chatbotPopup.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)";
  chatbotPopup.style.display = "none";
  chatbotPopup.style.flexDirection = "column";
  chatbotPopup.style.overflow = "hidden";
  document.body.appendChild(chatbotPopup);

  const chatbotHeader = document.createElement("div");
  chatbotHeader.style.backgroundColor = "#007bff";
  chatbotHeader.style.color = "#fff";
  chatbotHeader.style.padding = "10px";
  chatbotHeader.innerText = "Chatbot";
  chatbotPopup.appendChild(chatbotHeader);

  const chatbotMessages = document.createElement("div");
  chatbotMessages.style.flex = "1";
  chatbotMessages.style.padding = "10px";
  chatbotMessages.style.overflowY = "auto";
  chatbotPopup.appendChild(chatbotMessages);

  const chatbotInputContainer = document.createElement("div");
  chatbotInputContainer.style.display = "flex";
  chatbotInputContainer.style.borderTop = "1px solid #ccc";
  chatbotPopup.appendChild(chatbotInputContainer);

  const chatbotInput = document.createElement("input");
  chatbotInput.type = "text";
  chatbotInput.placeholder = "Type your question...";
  chatbotInput.style.flex = "1";
  chatbotInput.style.border = "none";
  chatbotInput.style.padding = "10px";
  chatbotInputContainer.appendChild(chatbotInput);

  const chatbotSendButton = document.createElement("button");
  chatbotSendButton.innerText = "Send";
  chatbotSendButton.style.backgroundColor = "#007bff";
  chatbotSendButton.style.color = "#fff";
  chatbotSendButton.style.border = "none";
  chatbotSendButton.style.padding = "10px";
  chatbotSendButton.style.cursor = "pointer";
  chatbotInputContainer.appendChild(chatbotSendButton);

  chatbotButton.addEventListener("click", function () {
    chatbotPopup.style.display =
      chatbotPopup.style.display === "none" ? "flex" : "none";
  });

  chatbotSendButton.addEventListener("click", function () {
    const question = chatbotInput.value.trim();
    if (question) {
      const userMessage = document.createElement("div");
      userMessage.innerText = "You: " + question;
      userMessage.style.marginBottom = "10px";
      chatbotMessages.appendChild(userMessage);

      fetch(`/chatbot-response/?question=${encodeURIComponent(question)}`)
        .then((response) => response.json())
        .then((data) => {
          const botMessage = document.createElement("div");
          botMessage.innerText = "Bot: " + data.response;
          botMessage.style.marginBottom = "10px";
          chatbotMessages.appendChild(botMessage);
          chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        });

      chatbotInput.value = "";
    }
  });
});
