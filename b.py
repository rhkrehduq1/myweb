import streamlit as st

st.title('회뤈가입')








but_메인 = st.button('메인')
if but_메인:
    st.switch_page("login.py")