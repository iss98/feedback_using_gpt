import streamlit as st
import pandas as pd
import openai

@st.cache_data
def generate_df(item, problem, feedback, attempt):
    data = {
        "Item": item,
        "Problem": problem,
        "Feedback": feedback,
        "Attempt": attempt
    }
    df = pd.DataFrame(data)
    return df

@st.cache_resource
def process_string(text):
    text = text.strip()
    text = text.replace(","," ")
    return text

@st.cache_resource
def generate_fb(prompt, response):    
    fb =openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=[{"role": "system", "content": prompt}, {"role": "user", "content": response}])
    fb = fb.choices[0].message.content
    fb = process_string(fb)
    return fb