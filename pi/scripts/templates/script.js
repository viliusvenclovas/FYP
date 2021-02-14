window.addEventListener('load', pageLoad)

function pageLoad() {
  document.getElementById("help-btn").addEventListener("click", openWindow)
  console.log("Test")
}

function openWindow() {
  driveIndex = this.id
  document.getElementById("close").addEventListener("click", closeWindow)
  document.getElementById("help").style.display = "block";
}

// closes drive profile window
function closeWindow() {
  document.getElementById("help").style.display = "none"
}