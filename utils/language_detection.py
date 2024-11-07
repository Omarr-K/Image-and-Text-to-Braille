from langdetect import detect

def detect_language(text):
    lang = detect(text)
    if lang == 'ar':
        return 'ar'
    elif lang == 'it':
        return 'ita'
    else:
        return 'en'
