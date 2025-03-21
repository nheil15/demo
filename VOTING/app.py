from flask import Flask, jsonify, request
from flask_cors import CORS
from services.voter_service import VoterService
from services.officer_service import OfficerService
from services.candidate_service import CandidateService
from services.voting_service import VotingService

app = Flask(__name__)
CORS(app)

# ------------------ Voter Authentication ------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    voter_id = data.get("voterID")
    pin = data.get("PIN")
    
    voter_data = VoterService.login(voter_id, pin)
    
    if voter_data:
        return jsonify({"message": "Login successful!", "voter": voter_data}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/voter/<voter_id>", methods=["GET"])
def get_voter_info(voter_id):
    voter = VoterService.get_voter_info(voter_id)
    
    if voter:
        return jsonify(voter), 200
    return jsonify({"message": "Voter not found"}), 404

# ------------------ Officer Authentication ------------------

@app.route("/officer/login", methods=["POST"])
def officer_login():
    data = request.json
    officer_id = data.get("officerID")
    pin = data.get("PIN")
    
    officer_data = OfficerService.login(officer_id, pin)
    
    if officer_data:
        return jsonify({"message": "Login successful!", "officer": officer_data}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# ------------------ Candidate Management ------------------

@app.route("/candidates", methods=["GET"])
def get_candidates():
    candidates_data = CandidateService.get_candidates()
    return jsonify(candidates_data)

# ------------------ Voting System ------------------

@app.route("/submit_vote", methods=["POST"])
def submit_vote():
    data = request.json
    voter_id = data.get("voterID")
    votes = data.get("votes")
    
    result = VotingService.submit_vote(voter_id, votes)
    
    if result["success"]:
        return jsonify({"message": result["message"]}), 200
    return jsonify({"message": result["message"]}), result["status"]

# ------------------ Vote Count Display ------------------

@app.route("/vote_count", methods=["GET"])
def get_vote_count():
    vote_results = VotingService.get_vote_count()
    return jsonify({"votes": vote_results})

# ------------------ Voting Status ------------------

@app.route("/voting_status", methods=["GET"])
def get_voting_status():
    status = VotingService.get_voting_status()
    return jsonify(status)

@app.route("/close_voting", methods=["POST"])
def close_voting():
    VotingService.set_voting_status(False)
    return jsonify({"message": "Voting has been closed!"})

@app.route("/open_voting", methods=["POST"])
def open_voting():
    VotingService.set_voting_status(True)
    return jsonify({"message": "Voting is now open!"})

# ------------------ Run Flask App ------------------

if __name__ == "__main__":
    app.run(debug=True)
