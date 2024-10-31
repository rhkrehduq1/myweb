import streamlit as st

st.title('3단어 맞추기')

word = st.text_input("단어를 입력해주세요")


result = ''
if word[0] == 's':
    result += "🟢"
elif word[1] == 's' or word[2] == 's':
    result += "🟡"
else:
    result += "🔴"

if word[1] == 'u':
    result += "🟢"
elif word[0] == 'u' or word[2] == 'u':
    result += "🟡"
else:
    result += "🔴"

if word[2] == 'n':
    result += "🟢"
elif word[1] == 'n' or word[0] == 'n':
    result += "🟡"
else:
    result += "🔴"


st.title(result)


if result == '🟢🟢🟢':
    st.title("정답입니다.")
    st.balloons()



if word[0] == '' or word[1] == '' or word[2] == '':
    st.title('글자수가 부족해요')



# 단어1 = st.text_input('단어를 입력하세요',key='단어1')
# if 단어1 == S:
#     단어1 = 'green'
# elif 단어1 == U or 단어1 == N:
#     단어1 = 'yellow'
# else:
#     단어1 = 'red'
# # st.write(단어1)
# 단어1 = st.text_input('단어를 입력하세요',key='단어1')
# if 단어1 == S:
#     st.success("정답")
# elif 단어1 == U or 단어1 == N:
#     st.warning("위치가 달라요")
# else:
#     st.error("오답")



# 단어2 = st.text_input('단어를 입력하세요',key='단어2')
# if 단어2 == U:
#     단어2 = 'green'
# elif 단어2 == S or 단어2 == N:
#     단어2 = 'yellow'
# else:
#     단어2 = 'red'
# st.write(단어2)



# 단어3 = st.text_input('단어를 입력하세요',key='단어3')
# if 단어3 == N:
#     단어3 = 'green'
# elif 단어3 == U or 단어3 == S:
#     단어3 = 'yellow'
# else:
#     단어3 = 'red'
# st.write(단어3)








but_메인 = st.button('메인')
if but_메인:
    st.switch_page("login.py")