import re

def remove_special_characters(text):
    # Substituir caracteres especiais por espaços em branco
    cleaned_text = re.sub(r'[^a-zA-Z0-9á-úç\.\s]', ' ', text)
    cleaned_text = cleaned_text.title()
    return cleaned_text

