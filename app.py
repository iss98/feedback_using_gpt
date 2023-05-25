import streamlit as st
import openai

from functions import *
from prompt import *

#openai api key
openai.api_key = st.secrets["api_key"]

#학생들의 데이터를 다운로드 받기 위한 코드
item = []
problem = []
feedback = []
attempt = []
item1_a = 0

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
    item1_a +=1
    prompt = prompt_item1 + response
    fb = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", max_tokens=200, temperature=0)
    fb = fb["choices"][0]["text"]
    st.subheader(":robot_face: : GPT의 피드백")
    st.text(fb)
    item.append("1")
    problem.append(response)
    feedback.append(fb)
    attempt.append(item1_a)

else : st.text("문제를 푼 후 피드백 받기를 눌러보세요!")

if st.button("결과 제출하기"):
    download_results(item, problem, feedback, attempt)

st.text("문의 : iss9802@snu.ac.kr")