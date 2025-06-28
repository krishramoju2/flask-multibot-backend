from deep_translator import GoogleTranslator

def translate_input(message, lang):
    if lang == "en":
        return message
    try:
        return GoogleTranslator(source=lang, target='en').translate(message)
    except Exception:
        return message

def translate_output(message, lang):
    if lang == "en":
        return message
    try:
        return GoogleTranslator(source='en', target=lang).translate(message)
    except Exception:
        return message
