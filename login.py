import streamlit as st

st.title('단어 맞추기')


but_1 = st.button('3단어 맞추기')
if but_1:
    st.switch_page("pages/b.py")

but_2 = st.button('4단어 맞추기')
if but_2:
    st.switch_page("pages/c.py")

but_3 = st.button('5단어 맞추기')
if but_3:
    st.switch_page("pages/d.py")