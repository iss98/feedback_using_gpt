import streamlit as st
import openai

from functions import *
from prompt import *

#openai api key
openai.api_key = st.secrets["api_key"]

#학생들의 데이터를 다운로드 받기 위한 코드
if 'item' not in st.session_state:
    st.session_state['item'] = []
if 'problem' not in st.session_state:
    st.session_state['problem'] = []
if 'feedback' not in st.session_state:
    st.session_state['feedback'] = []
if 'attempt' not in st.session_state:
    st.session_state['attempt'] = []
if 'item_1a' not in st.session_state:
    st.session_state['item_1a'] = 0


#Header of page
st.title("GPT를 활용한 평가 및 피드백 :blue[데모버전]")
st.header("연구설명")
st.text("이 연구는 gpt를 이용한 평가 및 피드백을 학교 현장에서 적용할 수 있는지 확인하려고 합니다. 이 페이지는 데모 페이지입니다.")
st.divider()
st.header("앞으로 정해야하는 내용")
st.text("1. 어떤 문제를 활용해야하는지 정하기 \n 2. 어떤 prompt engineering을 사용할지 \n 3. 어떻게 하면 수업시간에 적용가능한지?")
st.divider()
st.header("문제 및 피드백 예시")
st.markdown("$A \div 3y/2 = 4x^{2}y + 2xy +6$ 일 때 다항식 $A$ 를 구하시오")
response = st.text_input(label = '답안 :')

if st.button("GPT한테 피드백 받기"):
    st.session_state['item_1a'] +=1
    prompt = prompt_item1 + response    
    # fb = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=200, temperature=0)
    # fb = fb["choices"][0]["text"]
    fb = "안녕하세요"
    st.session_state["item"].append(1)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_1a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_1a']}")
    
else : st.text("문제를 푼 후 피드백 받기를 눌러보세요!")

if st.button("결과 제출하기"):
    csv = generate_csv(st.session_state["item"], st.session_state["problem"], st.session_state["feedback"], st.session_state["attempt"])
    st.download_button(label = "Press to Download", data = csv, file_name = "file.csv", mime = "text/csv")

st.text("문의 : iss9802@snu.ac.kr")