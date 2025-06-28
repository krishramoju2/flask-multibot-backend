def get_bot_response(bot_name, message):
    bots = {
        "cybersecurity": lambda msg: f"[Cybersecurity Bot] Threat Analysis: {msg}",
        "space": lambda msg: f"[Space Bot] Orbital Insights: {msg}",
        "deepsea": lambda msg: f"[Deep Sea Bot] Oceanic Data: {msg}",
        "stocks": lambda msg: f"[Stock Bot] Market Forecasting: {msg}"
    }
    return bots.get(bot_name, lambda msg: "[Unknown Bot] This bot is not available.")(message)
