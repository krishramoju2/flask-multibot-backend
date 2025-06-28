from deep_translator import GoogleTranslator
import logging

logging.basicConfig(filename="logs/backend.log", level=logging.INFO)

def log_event(event_type, message):
    logging.info(f"{event_type.upper()}: {message}")

def translate_input(message, lang):
    if lang == "en":
        return message
    try:
        return GoogleTranslator(source=lang, target='en').translate(message)
    except Exception:
        log_event("translation_error", f"{lang}: {message}")
        return message

def translate_output(message, lang):
    if lang == "en":
        return message
    try:
        return GoogleTranslator(source='en', target=lang).translate(message)
    except Exception:
        log_event("translation_error", f"{lang}: {message}")
        return message
