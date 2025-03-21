document.addEventListener("DOMContentLoaded", function() {
    fetchVotingStatus();
});

function fetchVotingStatus() {
    fetch("http://127.0.0.1:5000/voting_status")
        .then(response => response.json())
        .then(data => {
            document.getElementById("votingStatus").innerText = data.isVotingOpen ? "Open" : "Closed";
        })
        .catch(error => console.error("Error fetching voting status:", error));
}

function openVoting() {
    fetch("http://127.0.0.1:5000/open_voting", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchVotingStatus(); // Refresh status
        })
        .catch(error => console.error("Error opening voting:", error));
}

function closeVoting() {
    fetch("http://127.0.0.1:5000/close_voting", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchVotingStatus(); // Refresh status
        })
        .catch(error => console.error("Error closing voting:", error));
}

function showVoteCount() {
    window.location.href = "vote_count.html";
}

document.addEventListener("DOMContentLoaded", fetchVotingStatus);