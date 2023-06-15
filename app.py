import streamlit as st
from prompt import *
from functions import *
import openai

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
if 'item_2a' not in st.session_state:
    st.session_state['item_2a'] = 0
if 'item_3a' not in st.session_state:
    st.session_state['item_3a'] = 0
if 'item_4a' not in st.session_state:
    st.session_state['item_4a'] = 0
if 'item_5a' not in st.session_state:
    st.session_state['item_5a'] = 0


#Header of page
st.title("일차방정식 풀이 및 활용 문제")
name = st.text_input("이름")
number = st.text_input("번호")
st.divider()
st.header("문제를 풀고 피드백 받는 순서!")
st.write("1. 이름과 번호를 페이지의 가장 위에 입력해주세요")
st.write("2. 문제를 읽고 풀이칸에 자신의 풀이를 입력해주세요")
st.write("3. 피드백 받기 버튼을 눌러서 인공지능의 피드백을 읽어보세요")
st.write("4. 피드백을 바탕으로 문제를 다시 풀고 싶은 경우, 풀이칸에 다시 풀이를 적고 피드백 받기 버튼을 누르는 과정을 반복하세요")
st.divider()
st.header("1번")
st.markdown("다음 일차방정식을 푸시오. $0.3x + 2 = 0.1x + 0.8$")
response = st.text_input("풀이 : ", key = "input1")

if st.button("피드백 받기", key = "1"):
    st.session_state['item_1a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt1, response)
    st.session_state["item"].append(1)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_1a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_1a']}")
    
    
else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.divider()

st.header("2번")
st.markdown("다음 일차방정식을 푸시오 $2x + 13 = -3x -12$")
response = st.text_input("풀이 : ", key = "input2")

if st.button("피드백 받기", key = "2"):
    st.session_state['item_2a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt2, response)
    st.session_state["item"].append(2)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_2a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_2a']}")
    
else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.divider()
st.header("3번")
st.markdown("하민이와 민혁이는 종이를 접어 장미꽃을 만들기로 하였다. 하민이는 10분에 장미꽃 4송이를, 민혁이는 12분에 장미꽃 6송이를 만들 수 있다. 하민이와 민혁이가 집에서 각각 장미꽃 16송이와 12송이를 미리 만들어 와서 동시에 장미꽃을 만들기 시작하였다. 두 사람의 장미꽃의 개수가 같아지는 것은 장미꽃을 만들기 시작한 지 몇 분 후인지 구하고, 그 풀이 과정을 쓰시오.")
response = st.text_input("풀이 : ", key = "input3")

if st.button("피드백 받기", key = "3"):
    st.session_state['item_3a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt3, response)
    st.session_state["item"].append(3)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_3a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_3a']}")
    
else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.divider()

st.header("4번")
st.markdown("연속하는 세 자연수의 합이 $30$일 때, 이 세 자연수 중에서 가장 큰 자연수의 값을 자세한 설명과 함께 구하시오.")
response = st.text_input("풀이 : ", key = "input4")

if st.button("피드백 받기", key = "4"):
    st.session_state['item_4a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt4, response)
    st.session_state["item"].append(4)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_4a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_4a']}")
    
else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.divider()

st.header("5번")
st.markdown("연속한 두 수의 합이 $59$일 때, 큰 수를 구하세요.")
response = st.text_input("풀이 : ", key = "input5")

if st.button("피드백 받기", key = "5"):
    st.session_state['item_5a'] +=1
    response = process_string(response)
    fb = generate_fb(prompt5, response)
    st.session_state["item"].append(5)
    st.session_state["problem"].append(response)
    st.session_state["feedback"].append(fb)
    st.session_state["attempt"].append(st.session_state['item_5a'])
    st.subheader(":robot_face: : GPT의 피드백")
    st.write(fb)
    st.write(f"시도회수 {st.session_state['item_5a']}")
    
else : st.text("문제를 풀고 피드백 받기를 눌러보세요!")

st.divider()

if st.button("결과 다운로드받기"):
    df = generate_df(st.session_state["item"], st.session_state["problem"], st.session_state["feedback"], st.session_state["attempt"])
    csv = df.to_csv(index = False, encoding="cp949")
    st.download_button(label = "눌러서 파일 다운로드 받기", data = csv, file_name = f"{name}_{number}.csv")