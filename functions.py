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
    csv_data = df.to_csv(index=False, encoding="euc-kr")
    return csv_data