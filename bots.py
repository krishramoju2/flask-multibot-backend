import random

# Preloaded responses
bot_data = {
    "cybersecurity": {
        "keywords": ["ransomware", "lockbit", "phishing"],
        "responses": [
            "Zero-trust is now standard practice.",
            "AI-enhanced SOCs reduce breach detection time.",
            "Deepfake phishing is a major concern.",
        ],
    },
    "space": {
        "keywords": ["mars", "moon", "telescope"],
        "responses": [
            "Artemis III preps for 2026 Moon landing.",
            "JWST is sending deep field images of early galaxies.",
            "ESA's ExoMars mission resumes under new leadership.",
        ],
    },
    "deepsea": {
        "keywords": ["mariana", "thermal", "ocean"],
        "responses": [
            "AI gliders explore thermal vents autonomously.",
            "UN regulates mining below 6,000m.",
            "Plastic pollution detected even at 10,000m.",
        ],
    },
    "stocks": {
        "keywords": ["tesla", "market", "nifty"],
        "responses": [
            "Nifty50 hits record high after RBI policy changes.",
            "AI-based ETFs outperform traditional funds.",
            "2025 sees renewed interest in semiconductor stocks.",
        ],
    },
}

def get_bot_response(bot_name, message):
    message = message.lower()
    if bot_name not in bot_data:
        return "[Unknown Bot] No such specialization exists."

    bot = bot_data[bot_name]
    if any(word in message for word in bot["keywords"]):
        return bot["responses"][0]
    return random.choice(bot["responses"])
