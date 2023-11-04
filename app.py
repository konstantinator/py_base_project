import streamlit as st
import joblib
from scipy.sparse import hstack
from scipy.sparse import csr_matrix
from catboost import CatBoostRegressor
import re
from pymorphy2 import MorphAnalyzer


morph = MorphAnalyzer()
patterns = r'[^a-zA-Zа-яА-Я0-9ёЁ]'


def lemmatize(doc):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token:
            token = token.strip()
            token = morph.normal_forms(token)[0]
            tokens.append(token)
    if len(tokens) > 2:
        return tokens
    return []


def process():
    # Ввод текста
    reg = CatBoostRegressor()     
    reg.load_model('./models/model.cbm')
    tf_full = joblib.load('./models/vectorizer_full.pkl')

    st.title("Оценка сложности текстов на основе данных статей N+1")
    title = st.text_input("Заголовок")
    body = st.text_area("Введите основной текст", height=200)

    full_vec = tf_full.transform([title + ' ' + body])

    if st.button('Нажми меня'):
        len_body = csr_matrix(len(body))
        full_vec = hstack((tf_full.transform([' '.join(lemmatize(title)) + ' ' + ' '.join(lemmatize(body)) ]), 
                            len_body
        ))
        st.header(f"Оценка сложности текста: {round(reg.predict(full_vec)[0], 2)}")
        

if __name__=='__main__':
    process()
