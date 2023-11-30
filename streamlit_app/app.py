import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    # https://huggingface.co/facebook/wmt19-ru-en
    model = pipeline("translation", "facebook/wmt19-ru-en")
    return model


translator = load_model()
st.title('Переводчик')
text = st.text_area('Введите текст на русском языке')
result = translator(text)


if (text and result[0] and result[0]["translation_text"]):
    st.write('**Перевод:**\n')
    st.write(result[0]["translation_text"])
