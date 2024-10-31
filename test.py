import streamlit as st

st.title('단어 맞추기')



st.write('다음중 프로그램에 대한 설명으로 가장적절한 것은?')
결과 = st.radio('보기',['파이선을 배운다','10주 동안 수업을 한다.','3번 결석해도 괜찮다.','재미없다.'])
btn = st.button('정답확인')
if btn: