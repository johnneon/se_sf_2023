from transformers import pipeline

translator = pipeline("translation", "facebook/wmt19-ru-en")

def translate(text: str) -> str:
    result = translator(text)
    return result[0]['translation_text']
