// static/script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) { // Ensure the form exists before adding event listener
        form.addEventListener("submit", () => {
            alert("Calculating your home's estimated price... Please wait.");
        });
    }
});