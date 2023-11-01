import streamlit as st
import joblib
from scipy.sparse import hstack
from catboost import CatBoostRegressor


def process():
    reg = CatBoostRegressor()      # parameters not required.
    reg.load_model('model.cbm')
    tf_full = joblib.load('vectorizer_full.pkl')

    # Название
    st.title("Оценка сложности текстов на основе данных статей N+1")

    # Заголовок
    st.header("Введите заголовок")

    title = st.text_input("Заголовок")
    body = st.text_area("Введите основной текст", height=200)

    # if title and body:
    full_vec = tf_full.transform([title + ' ' + body])

    if st.button('Нажми меня'):
        st.header(f"Оценка сложности текста {round(reg.predict(full_vec)[0], 2)}")
        

if __name__=='__main__':
    process()
