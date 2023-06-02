import streamlit as st
import pandas as pd
import openai

def generate_df(item, problem, feedback, attempt):
    data = {
        "Item": item,
        "Problem": problem,
        "Feedback": feedback,
        "Attempt": attempt
    }
    df = pd.DataFrame(data)
    return df

def process_string(text):
    text = text.strip()
    text = text.replace(","," ")
    return text

def get_text(key):
    input_text = st.text_input("답안 : ", key = key)
    return input_text

def generate_fb(prompt, response):
    prompt = prompt + response    
    fb = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=200, temperature=0)
    fb = fb["choices"][0]["text"]
    fb = process_string(fb)
    return fb