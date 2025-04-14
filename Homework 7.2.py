def correct_sentence(text):
    if not text.endswith('.'):
        text += '.'
    return text[0].upper() + text[1:]

