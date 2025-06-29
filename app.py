from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

BOT_MEMORY_FILE = "bot_memory.json"
SESSION_LOG_DIR = "session_logs"

# Ensure session log directory exists
os.makedirs(SESSION_LOG_DIR, exist_ok=True)

# Global bot status tracking dictionary
bot_status = {}

# Load bot memory from JSON
def load_bot_memory():
    with open(BOT_MEMORY_FILE, "r") as f:
        return json.load(f)

# Initialize all bots as healthy and available
def init_bot_status():
    memory = load_bot_memory()
    for bot in memory:
        bot_status[bot] = {
            "status": "healthy",
            "available": True,
            "last_used": "Never"
        }

# Log when a bot is used
def update_bot_last_used(bot_name):
    if bot_name in bot_status:
        bot_status[bot_name]["last_used"] = datetime.now().isoformat()

# Save chat history for a session
def save_session(session_id, bot_name, user_input, bot_response, language):
    path = os.path.join(SESSION_LOG_DIR, f"{session_id}.json")
    session = []

    if os.path.exists(path):
        with open(path, "r") as f:
            session = json.load(f)

    session.append({
        "timestamp": datetime.now().isoformat(),
        "bot": bot_name,
        "lang": language,
        "prompt": user_input,
        "response": bot_response
    })

    with open(path, "w") as f:
        json.dump(session, f, indent=2)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id = data.get("session_id")
    user_input = data.get("message")
    language = data.get("language", "en")
    bot_name = data.get("bot_name")

    bot_memory = load_bot_memory()

    if bot_name not in bot_memory:
        return jsonify({"error": "Bot not found"}), 404

    response = None
    for kw, resp in zip(bot_memory[bot_name]["keywords"], bot_memory[bot_name]["responses"]):
        if kw.lower() in user_input.lower():
            response = resp
            break

    if not response:
        response = f"[{bot_name}] I couldn't find an answer to your query."

    # Update bot status & session memory
    update_bot_last_used(bot_name)
    save_session(session_id, bot_name, user_input, response, language)

    return jsonify({"response": response})

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(bot_status)

if __name__ == "__main__":
    init_bot_status()
    app.run(debug=True, host="0.0.0.0", port=8000)
