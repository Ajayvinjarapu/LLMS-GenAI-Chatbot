from google import genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

while True:

    question = input("Ask question to chatbot: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print("Chatbot:", response.text)