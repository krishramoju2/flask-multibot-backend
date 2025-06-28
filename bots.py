import random

def get_bot_response(bot_name, message):
    message_lower = message.lower()

    if bot_name == "cybersecurity":
        if "ransomware" in message_lower:
            return "Ransomware attacks have evolved with AI-generated phishing in 2025. SOC teams now use behavioral AI for detection."
        elif "phishing" in message_lower:
            return "2025 phishing attacks often spoof QR codes and use deepfake voice assistants to deceive users."
        return random.choice([
            "Zero-trust architecture adoption increased by 45% in 2025.",
            "Major 2025 breaches included healthcare and cloud storage providers.",
            "AI-driven anomaly detection is now standard in SOC operations."
        ])

    elif bot_name == "space":
        if "mars" in message_lower:
            return "Mars Sample Return is scheduled for 2026. The 2025 rover is caching soil near Jezero crater."
        elif "moon" in message_lower:
            return "NASA's Artemis III will land on the Moon in 2026. Preparations began mid-2025 with successful booster tests."
        return random.choice([
            "SpaceX launched 150+ Starlink satellites this year.",
            "ESA’s ExoMars mission restarted with AI navigation systems.",
            "Commercial lunar payloads are scheduled monthly in 2025."
        ])

    elif bot_name == "deepsea":
        if "mariana" in message_lower:
            return "Exploration of the Mariana Trench in 2025 revealed microbial life thriving in high-pressure thermal vents."
        elif "submarine" in message_lower:
            return "Autonomous submarines now map ocean trenches in real-time using sonar and AI-based terrain modeling."
        return random.choice([
            "Deep-sea mining is regulated under 2025 UN marine rules.",
            "AI drones discovered new sponge colonies below 6000m.",
            "Plastic waste was detected even at 10,000m depth in recent missions."
        ])

    elif bot_name == "stocks":
        if "tesla" in message_lower:
            return "Tesla's stock fluctuated in Q2 2025 due to China's EV market changes and FSD regulation updates."
        elif "nifty" in message_lower:
            return "Nifty50 crossed 24,000 in June 2025 amid IT and banking sector gains."
        return random.choice([
            "AI-driven ETFs outperformed traditional indices by 12% YTD.",
            "Investors are watching Fed's July 2025 inflation forecast closely.",
            "2025 Q2 earnings show recovery in semiconductor sectors."
        ])

    else:
        return "[Unknown Bot] This bot specialization doesn't exist."
