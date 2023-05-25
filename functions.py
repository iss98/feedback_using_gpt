import pandas as pd
import base64
import streamlit as st

def generate_csv(item, problem, feedback, attempt):
    data = {
        "Item": item,
        "Problem": problem,
        "Feedback": feedback,
        "Attempt": attempt
    }
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False, encoding="utf-8-sig")
    return csv_data

def download_results(item, problem, feedback, attempt):
    csv = generate_csv(item, problem, feedback, attempt)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="quiz_results.csv">다운로드</a>'
    st.markdown(href, unsafe_allow_html=True)