import streamlit as st
import google.generativeai as genai

# Wannan zai nuna mana idan akwai matsala da Key din
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    # Mu nuna harafin farko da na karshe kawai don mu tabbatar sabo ne
    st.write(f"An kwaso Key mai farawa da: {api_key[:5]}... da kuma karshen: ...{api_key[-4:]}")
    genai.configure(api_key=api_key)
else:
    st.error("Ba a saka GOOGLE_API_KEY a Secrets ba!")

model = genai.GenerativeModel("gemini-1.5-flash")

if p := st.chat_input("Research"):
    try:
        r = model.generate_content(p)
        st.write(r.text)
    except Exception as e:
        st.error(f"Har yanzu akwai matsala: {e}")
