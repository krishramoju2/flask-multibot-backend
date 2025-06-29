from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

BOT_MEMORY_FILE = "bot_memory.json"
SESSION_LOG_DIR = "session_logs"
DRIFT_LOG_DIR = "monthly_drift_logs"

os.makedirs(SESSION_LOG_DIR, exist_ok=True)
os.makedirs(DRIFT_LOG_DIR, exist_ok=True)

bot_status = {}

def load_bot_memory():
    with open(BOT_MEMORY_FILE, "r") as f:
        return json.load(f)

def init_bot_status():
    memory = load_bot_memory()
    for bot in memory:
        bot_status[bot] = {
            "status": "healthy",
            "available": True,
            "last_used": "Never"
        }

def update_bot_last_used(bot_name):
    if bot_name in bot_status:
        bot_status[bot_name]["last_used"] = datetime.now().isoformat()

def sanitize_input(text):
    blacklist = ["__import__", "eval", "exec", "open(", "os.", "subprocess", "socket", "system(", "sh"]
    for word in blacklist:
        if word.lower() in text.lower():
            return False
    return True

def validate_api_key(headers):
    return headers.get("X-API-Key") == API_KEY

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

def track_drift(bot_name, user_input, bot_response):
    month_key = datetime.now().strftime("%Y-%m")
    drift_file = os.path.join(DRIFT_LOG_DIR, f"{bot_name}_{month_key}.json")
    
    drift_log = []
    if os.path.exists(drift_file):
        with open(drift_file, "r") as f:
            drift_log = json.load(f)

    drift_log.append({
        "timestamp": datetime.now().isoformat(),
        "prompt": user_input,
        "response": bot_response
    })

    with open(drift_file, "w") as f:
        json.dump(drift_log, f, indent=2)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if not validate_api_key(request.headers):
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    session_id = data.get("session_id")
    user_input = data.get("message")
    language = data.get("language", "en")
    bot_name = data.get("bot_name")

    if not sanitize_input(user_input):
        return jsonify({"error": "Disallowed prompt"}), 400

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

    # Save logs and update health
    update_bot_last_used(bot_name)
    save_session(session_id, bot_name, user_input, response, language)
    track_drift(bot_name, user_input, response)

    return jsonify({"response": response})

@app.route("/status", methods=["GET"])
def get_status():
    if not validate_api_key(request.headers):
        return jsonify({"error": "Unauthorized"}), 403

    return jsonify(bot_status)

if __name__ == "__main__":
    init_bot_status()
    app.run(debug=True, host="0.0.0.0", port=8000)
