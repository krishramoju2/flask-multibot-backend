import random

def get_bot_response(bot_name, message):
    message = message.lower()

    if bot_name == "cybersecurity":
        if "ransomware" in message:
            return "2025: Ransomware is now being deployed via AI-coded malware kits."
        return random.choice([
            "Zero-day detection AI has grown 75% more accurate.",
            "Multi-cloud attack surfaces dominate 2025 threat maps.",
            "Phishing simulations have exposed 33% of employees."
        ])

    elif bot_name == "space":
        if "mars" in message:
            return "Mars orbiters now autonomously adjust orbits for max data yield."
        return random.choice([
            "NASA Artemis III Moon lander passed final preflight check in May 2025.",
            "China launched its 2nd lunar base module in Q2 2025.",
            "ISS AI assistants are now fully voice-interactive."
        ])

    elif bot_name == "deepsea":
        if "trench" in message:
            return "Microplastics found in deepest sediment layers of Kermadec trench."
        return random.choice([
            "2025 UN treaty limits seabed mining below 6,000m.",
            "AI-gliders now explore thermal vents autonomously.",
            "New species of bioluminescent fish discovered in Pacific abyss."
        ])

    elif bot_name == "stocks":
        if "tesla" in message:
            return "Tesla shares jumped after Q2 earnings beat in July 2025."
        return random.choice([
            "AI-powered ETFs outperformed S&P500 by 11% YTD.",
            "2025 markets react to renewed US-China trade optimism.",
            "Investors favor green hydrogen stocks amid new EU grants."
        ])

    return "[Unknown Bot] No such specialization exists."
