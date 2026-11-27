function generateVideo() {
  const status = document.getElementById("status");
  const prompt = document.querySelector("textarea").value.trim();

  if (!prompt) {
    status.textContent = "Please enter a prompt.";
    return;
  }

  status.textContent = "AI Engine: Server not connected yet.";
}
