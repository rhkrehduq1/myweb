
import streamlit as st

st.title('다른거')
id = st.text_input('아이디')
pw = st.text_input('비밀번호',
                   type='password')
btn = st.button('확인')

if btn:
    if id=='abc' and pw == '123':
        st.success('로그인 성공!!')
    else:
        st.error('로그인 실패!!')



but_메인 = st.button('메인')
if but_메인:
    st.switch_page("login.py")