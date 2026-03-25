import streamlit as st
import google.generativeai as genai

# Wannan zai dauko API Key daga asirin Streamlit (Secrets)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

instruction = "Sunanka Assistant AI 2026. Kai mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu."
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instruction)

st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg")
st.title("🤖 Assistant AI 2026")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Research"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    try:
        r = model.generate_content(p)
        with st.chat_message("assistant"): st.markdown(r.text)
        st.session_state.messages.append({"role": "assistant", "content": r.text})
    except Exception as e:
        st.error(f"Kuskure: {e}")
