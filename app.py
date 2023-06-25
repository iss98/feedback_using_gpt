import streamlit as st
from prompt import *
from functions import *
import openai

#openai api key
openai.api_key = st.secrets["api_key"]


#학생들의 데이터를 다운로드 받기 위한 코드
if 'item' not in st.session_state:
    st.session_state['item'] = []

if 'answer' not in st.session_state:
    st.session_state['answer'] = []
if 'feedback' not in st.session_state:
    st.session_state['feedback'] = []
if 'conf' not in st.session_state:
    st.session_state['conf'] = []
if 'sat' not in st.session_state:
    st.session_state['sat'] = []



#Header of page
st.title("일차방정식 활용 문제 과정 중심 평가가")
name = st.text_input("이름")
st.divider()
st.header("평가 순서!")
st.write("1. 이름을 입력해주세요")
st.write("2. 문제를 읽고 풀이칸에 자신의 풀이를 입력해주세요")
st.write("3. 풀이를 적고, 풀이에 대한 자신감과 직전 피드백이 풀이 작성에 도움이 되었는지 체크해주세요(첫번째 작성이라면 첫번째 답변임을 골라주세요)")
st.write("4. 피드백 받기 버튼을 눌러서 인공지능의 피드백을 읽어보세요")
st.write("5. 피드백을 읽은 후 풀이칸에 다시 풀이를 적고 피드백 받기 버튼을 다시 눌러주세요(2번 이상 풀어보기!!)")
st.write("6. 문제를 모두 풀고 결과 다운로드 받기 > 눌러서 파일 다운로드 받기를 눌러 풀이 결과를 파일로 다운로드 받으세요")
st.write("7. 다운로드 받은 파일을 아래의 링크에 들어가서 설문과 함께 제출해주세요")
st.markdown("[구글 설문 링크](https://forms.gle/qhKB7WkYcxFwn4gL9)")
st.divider()
st.header("피드백을 받는 방법")
st.write("1. 좋은 피드백을 받기 위해서, 풀이를 최대한 상세하게 적어보세요!")
st.write("2. 문제를 모두 푼 다음에 피드백을 받을 필요는 없습니다. 문제를 푸다가 막히는 부분이 있으면, 푼 곳 까지만 적어서 피드백을 받아보세요")
st.write("3. 피드백을 받은 후, 피드백에 따라 풀이를 수정해서 다시 피드백을 받아보세요! 풀이 -> 피드백 -> 다시 풀이의 과정을 반복해봐요!")
st.divider()
st.header("1번")
st.markdown("다음 일차방정식을 푸시오. $2x + 13 = -3x -12$")
text_placeholder = st.empty()
response = text_placeholder.text_input("풀이과정과 함께 답을 쓰시오 : ", key = "input1")
confidence = st.radio("당신의 풀이에 얼마나 자신감이 있으신가요?", ["선택하지 않음", "매우 아니다", "아니다", "그렇다", "매우 그렇다"])
stat = st.radio("피드백이 학습에 효과적인가요?", ["첫번째 답변임", "매우 아니다", "아니다", "그렇다", "매우 그렇다"])
if st.button("피드백 받기", key = "1"):
    fb = generate_fb(prompt1, response)
    st.write("**GPT의 피드백**")
    st.write(fb)
    response = process_string(response)
    fb = process_string(fb)
    st.session_state["item"].append("1")
    st.session_state["answer"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["conf"].append(confidence)
    st.session_state["sat"].append(stat)

else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.subheader("학습활동기록")
if st.session_state["item"] != []:
    for i, a in enumerate(st.session_state["item"]):
        st.write(a + "번문제")
        st.write(":student: : " + st.session_state["answer"][i])
        st.write(":robot_face: : " + st.session_state["feedback"][i])
        
st.divider()


if st.button("결과 다운로드받기"):
    df = generate_df(st.session_state["answer"], st.session_state["feedback"], st.session_state["conf"], st.session_state["sat"])
    csv = df.to_csv(index = False, encoding="cp949")
    st.download_button(label = "눌러서 파일 다운로드 받기", data = csv, file_name = f"{name}.csv")

st.divider()
st.write("7. 다운로드 받은 파일을 아래의 링크에 들어가서 설문과 함께 제출해주세요")
st.markdown("[구글 설문 링크](https://forms.gle/qhKB7WkYcxFwn4gL9)")