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
    if any(word in message for word in ["ransomware", "encryption", "lockbit"]):
        return "Ransomware gangs in 2025 are using AI-generated code and triple extortion techniques. LockBit 3.0 remains active."
    elif any(word in message for word in ["phishing", "spoof", "email scam", "deepfake"]):
        return "Phishing campaigns now use voice deepfakes and QR-code redirection attacks. Stay vigilant."
    elif any(word in message for word in ["zero-day", "vulnerability", "exploit"]):
        return "Zero-day vulnerabilities are being stockpiled by state actors. Patch management is critical."
    elif any(word in message for word in ["ai", "ml", "machine learning", "automation"]):
        return "AI-based threat detection tools now outperform traditional firewalls by 42%."
    else:
        return random.choice([
            "Credential stuffing attacks surged in 2025 due to leaked password datasets.",
            "Cyber-insurance premiums rose due to increasing breach frequency.",
            "SIEM systems now integrate behavioral analytics by default."
        ])


def get_space_response(message):
    if any(word in message for word in ["mars", "perseverance", "jezero"]):
        return "Mars exploration continues with Perseverance and Sample Return missions. AI navigation helps avoid rocky terrain."
    elif any(word in message for word in ["moon", "artemis", "lunar"]):
        return "Artemis III aims for crewed lunar landing in 2026. Lunar Gateway construction has begun in orbit."
    elif any(word in message for word in ["satellite", "starlink", "orbit"]):
        return "Starlink now has 6,000+ active satellites, enabling global low-latency internet access."
    elif any(word in message for word in ["asteroid", "defense", "impact", "nasa dart"]):
        return "NASA’s planetary defense team tracks over 30,000 near-earth objects using DART and infrared satellites."
    else:
        return random.choice([
            "The James Webb Space Telescope is delivering high-res galaxy cluster images.",
            "Private spaceflight doubled in 2025 due to new launch providers.",
            "China's Tianwen-2 is targeting asteroid 469219 Kamoʻoalewa."
        ])


def get_deepsea_response(message):
    if any(word in message for word in ["mariana", "trench", "deepest"]):
        return "Mariana Trench probes found new anaerobic bacteria capable of metabolizing plastics at depth."
    elif any(word in message for word in ["hydrothermal", "vents", "lava", "sulfur"]):
        return "Hydrothermal vent ecosystems thrive in total darkness, supported by chemosynthetic bacteria."
    elif any(word in message for word in ["submarine", "rov", "glider", "drone"]):
        return "Underwater drones in 2025 can operate autonomously for 6 months, mapping trenches and collecting samples."
    elif any(word in message for word in ["plastic", "pollution", "microplastic"]):
        return "Microplastics are now detected in every ocean trench, down to depths over 10,000 meters."
    else:
        return random.choice([
            "Deep-sea mining faces ethical and ecological scrutiny worldwide.",
            "The Indian Ocean expedition discovered over 80 new marine species.",
            "Marine biologists use AI to analyze sonar and photometric data."
        ])


def get_stocks_response(message):
    if any(word in message for word in ["tesla", "ev", "elon", "autopilot"]):
        return "Tesla's Q2 2025 performance beat forecasts. Cybertruck delivery targets are on track."
    elif any(word in message for word in ["nifty", "sensex", "india"]):
        return "Nifty50 surged past 24,000 due to strong earnings in IT and banking. FIIs returned after policy easing."
    elif any(word in message for word in ["inflation", "cpi", "fed", "interest rates"]):
        return "US Fed signals potential rate cuts by late 2025 as inflation stabilizes around 3%."
    elif any(word in message for word in ["ai", "etf", "semiconductors", "chip"]):
        return "AI-focused ETFs outpaced S&P 500 by 14% in H1 2025, driven by semiconductor demand and enterprise AI adoption."
    else:
        return random.choice([
            "Retail investors are moving towards mid-cap momentum stocks.",
            "China's property market shows signs of stabilization.",
            "Crypto ETFs gained regulatory clarity in 2025 Q2."
        ])
