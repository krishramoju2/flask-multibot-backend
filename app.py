from flask import Flask, request, jsonify, render_template
from bots import get_bot_response
from memory import session_memory
from utils import translate_input, translate_output
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id = data.get("session_id")
    user_input = data.get("message")
    language = data.get("language", "en")
    bot_name = data.get("bot_name")

    if session_id not in session_memory:
        session_memory[session_id] = []

    # Translate input if needed
    translated_input = translate_input(user_input, language)

    session_memory[session_id].append(("user", translated_input))
    bot_reply = get_bot_response(bot_name, translated_input)
    session_memory[session_id].append((bot_name, bot_reply))

    # Translate back to user's language
    translated_reply = translate_output(bot_reply, language)

    return jsonify({
        "reply": translated_reply,
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
