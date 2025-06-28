import json
import random

with open("bot_config.json", "r") as f:
    bot_data = json.load(f)

def get_bot_response(bot_name, message):
    message = message.lower()
    if bot_name not in bot_data:
        return "[Unknown Bot] No such specialization exists."

    bot = bot_data[bot_name]
    if any(word in message for word in bot["keywords"]):
        return bot["responses"][0]
    return random.choice(bot["responses"])
