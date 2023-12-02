import streamlit as st
from transformers import pipeline



@st.cache_resource
def load_model():
    # https://huggingface.co/facebook/wmt19-ru-en
    model = pipeline("translation", "facebook/wmt19-ru-en")
    return model

def translate(text):
    translator = load_model()
    result = translator(text)
    return result

def get_dict():
    return { 'title': 'Переводчик', 'main_text': 'Введите текст на русском языке', 'result_text': '**Перевод:**\n' }


def main():
    dict = get_dict()
    st.title(dict['title'])
    text = st.text_area(dict['main_text'])
    result = translate(text)


    if (text and result[0] and result[0]["translation_text"]):
        st.write(dict['result_text'])
        st.write(result[0]["translation_text"])


if __name__ == '__main__':
    main()