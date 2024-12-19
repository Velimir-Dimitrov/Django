document.addEventListener("DOMContentLoaded", function () {
    const messages = document.getElementById("message-container");
    if (messages) {
        setTimeout(() => {
            messages.style.transition = "opacity 1.5s ease-out";
            messages.style.opacity = "0";
            setTimeout(() => messages.remove(), 5000);
        }, 3000);
    }
});