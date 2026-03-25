import streamlit as st
import google.generativeai as genai

# Kar ka saka API Key anan, bar shi a haka
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("Ba a samu GOOGLE_API_KEY a cikin Secrets ba.")

# Saita Model (Gemini 1.5 Flash)
instruction = "Sunanka Assistant AI 2026. Kai mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu."
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instruction)

# Tsarin Fuskar Website
st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg")
st.title("🤖 Assistant AI 2026")
st.caption("Mataimakin Ilimi da Bincike")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Sashin Research
if p := st.chat_input("Research"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    try:
        response = model.generate_content(p)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Kuskuren API: {e}")
