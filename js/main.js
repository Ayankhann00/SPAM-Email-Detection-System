document.getElementById("checkBtn").addEventListener("click", function () {
  let message = document.getElementById("messageInput").value.trim();
  let resultBox = document.getElementById("result");

  if (message === "") {
    resultBox.innerHTML = "⚠️ Please enter some text.";
    resultBox.style.color = "orange";
    return;
  }

  // Simulating a result (replace with backend API call in Django)
  let isSpam = Math.random() > 0.5; // Random spam detection for demo

  if (isSpam) {
    resultBox.innerHTML = "🚨 This message is likely SPAM!";
    resultBox.style.color = "red";
  } else {
    resultBox.innerHTML = "✅ This message seems safe.";
    resultBox.style.color = "lightgreen";
  }
});
