document.getElementById("officerLoginForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const officerID = document.getElementById("officerid").value;
    const officerPIN = document.getElementById("officerpin").value;

    fetch("http://127.0.0.1:5000/officer/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ officerID: officerID, PIN: officerPIN })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Login successful!") {
            alert("Login successful!");
            window.location.href = "manage.html";  
        } else {
            document.getElementById("loginMessage").textContent = "Invalid credentials. Please try again.";
        }
    })
    .catch(error => console.error("Error:", error));
});