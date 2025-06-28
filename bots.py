import random

def get_bot_response(bot_name, message):
    message = message.lower()

    if bot_name == "cybersecurity":
        return get_cybersecurity_response(message)
    elif bot_name == "space":
        return get_space_response(message)
    elif bot_name == "deepsea":
        return get_deepsea_response(message)
    elif bot_name == "stocks":
        return get_stocks_response(message)
    else:
        return "[Unknown Bot] No such specialization exists."

def get_cybersecurity_response(message):
    if any(word in message for word in ["ransomware", "lockbit", "phishing"]):
        return "Cybersecurity in 2025 faces AI ransomware and QR phishing threats."
    return random.choice([
        "Zero-trust is now standard practice.",
        "AI-enhanced SOCs reduce breach detection time.",
        "Deepfake phishing is a major concern."
    ])

def get_space_response(message):
    if "mars" in message:
        return "Perseverance rover continues sample caching missions on Mars."
    return random.choice([
        "Artemis III preps for 2026 Moon landing.",
        "JWST is sending deep field images of early galaxies.",
        "ESA's ExoMars mission resumes under new leadership."
    ])

def get_deepsea_response(message):
    if "mariana" in message:
        return "New microbial life discovered in the Mariana Trench in 2025."
    return random.choice([
        "AI gliders explore thermal vents autonomously.",
        "UN regulates mining below 6,000m.",
        "Plastic pollution detected even at 10,000m."
    ])

def get_stocks_response(message):
    if "tesla" in message:
        return "Tesla stock soared after Q2 2025 earnings beat."
    return random.choice([
        "Nifty50 hits record high after RBI policy changes.",
        "AI-based ETFs outperform traditional funds.",
        "2025 sees renewed interest in semiconductor stocks."
    ])
