// static/script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", () => {
        alert("Sending request to server... Please wait.");
    });
});
