import streamlit as st

st.title('단어 맞추기')

but_게임시작 = st.button('게임사작')
if but_게임시작:
    st.switch_page("/pages/c.py")

단어 = st.text_input('단어를 입력하세요')

st.write(단어)

