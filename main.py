import streamlit as st


st.write('다음중 프로그램에 대한 설명으로 가장적절한 것은?')
결과 = st.radio('보기',['파이선을 배운다','10주 동안 수업을 한다.','3번 결석해도 괜찮다.','재미없다.'])
btn = st.button('정답확인')
if btn:
    if 결과 == '파이선을 배운다':
        st.success('정답')
        st.balloons()
    else:
        st.error('오답')

slider = st.select_slider('반을 선택하세요',['1반','2반','3반','4반'])

st.video('https://www.youtube.com/watch?v=JF0YwScEMag')

과학 = st.multiselect('과학탐구 과목을 선택하세요',['물리','하학','생물','지구'],max_selections=2)

st.write(과학)

과목 = st.selectbox('과목을 선택하세요',['확통','미적','기하'])

st.write('당신이 선택한 과목은 '+과목+'입니다.')

색상 = st.radio('당신이 좋아하는 색상은?',  ['빨강','노랑','파랑'])

st.write(색상+'을 좋아하시네요?')





짜장면=st.checkbox('짜장면 5000원')
짬뽕=st.checkbox('짬뽕 6000원')


가격 = 0
if 짜장면:
    가격+=5000
if 짬뽕:
    가격+=6000

if 가격 != 0:
    st.write(str(가격)+'원 입니다.')


st.title('🍜title')
st.header('header')
st.subheader('subheader')
st.write('**곽도엽**님 안녕하세요')
st.write(':rainbow[함지고등학교]')

st.title('로그인')
id = st.text_input('아이디')
pw = st.text_input('비밀번호',
                   type='password')
btn = st.button('확인')

if btn:
    if id=='abc' and pw == '123':
        st.success('로그인 성공!!')
    else:
        st.error('로그인 실패!!')