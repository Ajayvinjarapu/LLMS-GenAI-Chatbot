# import streamlit as st
# import google.generativeai as genai

# api_key = st.secrets["GEMINI_API_KEY"]

# genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-2.5-flash")

# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])

# st.title("Gemini Chatbot")

# user_input = st.text_input("Ask something")

# if st.button("Send"):
#     if user_input:
#         response = st.session_state.chat.send_message(user_input)
#         st.write(response.text)

import streamlit as st
import google.generativeai as genai
from prompts import prompts

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
st.title("Gemini Chatbot with Prompts")
option = st.selectbox("Choose a prompt", list(prompts.keys()))

if st.button("Generate Response"):
    
    prompt = prompts[option]
    
    response = model.generate_content(prompt)
    
    st.write(response.text)