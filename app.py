import streamlit as st
from prompt import *
from functions import *

#openai api key
openai.api_key = st.secrets["api_key"]

@st.cache_data
def main():
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
    if 'item_2a' not in st.session_state:
        st.session_state['item_2a'] = 0

name = st.text_input("이름")
number = st.text_input("번호")

main()

#Header of page
st.title("GPT를 활용한 평가 및 피드백 :blue[데모버전]")
st.header("연구설명")
st.write("이 연구는 gpt를 이용한 평가 및 피드백을 학교 현장에서 적용할 수 있는지 확인하려고 합니다. 이 페이지는 데모 페이지입니다.")
st.divider()
st.header("앞으로 정해야하는 내용")
st.write("1. 어떤 문제를 활용해야하는지 정하기 \n 2. 어떤 prompt engineering을 사용할지 \n 3. 어떻게 하면 수업시간에 적용가능한지?")
st.divider()
st.header("문제 및 피드백 예시")
st.markdown("$A \div 3y/2 = 4x^{2}y + 2xy +6$ 일 때 다항식 $A$ 를 구하시오")
response = get_text("input1")

if st.button("GPT한테 피드백 받기", key = "1"):
    st.session_state['item_1a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt_item1, response)
    st.session_state["item"].append(1)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_1a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_1a']}")
    
else : st.text("문제를 푼 후 피드백 받기를 눌러보세요!")

st.divider()
st.header("문제 및 피드백 예시")
st.markdown("$A \div 3y/2 = 4x^{2}y + 2xy +6$ 일 때 다항식 $A$ 를 구하시오")
response = get_text("input2")

if st.button("GPT한테 피드백 받기", key = "2"):
    st.session_state['item_2a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt_item1, response)
    st.session_state["item"].append(2)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_2a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_2a']}")
    
else : st.text("문제를 푼 후 피드백 받기를 눌러보세요!")



if st.button("결과 보기"):
    df = generate_df(st.session_state["item"], st.session_state["problem"], st.session_state["feedback"], st.session_state["attempt"])
    csv = df.to_csv(index = False, encoding="cp949")
    st.download_button(label = "결과 다운로드 받기", data = csv, file_name = f"{name}_{number}.csv")

st.text("문의 : iss9802@snu.ac.kr")