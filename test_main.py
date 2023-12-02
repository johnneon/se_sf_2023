from main import get_dict, translate

def test_dict():
    dict = get_dict()
    assert dict['title'] == 'Переводчик'
    assert dict['main_text'] == 'Введите текст на русском языке'
    assert dict['result_text'] == '**Перевод:**\n'

def test_translator_hi():
    result = translate('привет')
    assert result[0]['translation_text'] == 'hi'

def test_translator_new():
    result = translate('что нового')
    assert result[0]['translation_text'] == 'what\'s new'
