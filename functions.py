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
    csv_data = df.to_csv(index=False, encoding="utf-8")
    return csv_data

def download_results(item, problem, feedback, attempt):
    csv = generate_csv(item, problem, feedback, attempt)
    st.download_button("Press to Download", csv, "file.csv", "text/csv", key='download-csv')