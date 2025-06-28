import os
import json

LOG_DIR = "session_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_session_file(session_id):
    return os.path.join(LOG_DIR, f"{session_id}.json")

def load_session(session_id):
    file_path = get_session_file(session_id)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_session(session_id, history):
    file_path = get_session_file(session_id)
    with open(file_path, "w") as f:
        json.dump(history, f)
