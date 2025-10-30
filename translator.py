from googletrans import Translator

def translate_text(text, target_lang):
    """
    Translates the given text to the target language using Google Translate.

    Args:
        text (str): The text to translate.
        target_lang (str): The target language code (e.g., 'es' for Spanish).

    Returns:
        str: The translated text.
    """
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        return f"Translation error: {str(e)}"
