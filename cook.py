import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
st.title("Gemini API with Streamlit")
user_input = st.text_area("Enter your prompt here:")
if st.button("Generate Response"):
    if user_input:
        response = genai.generate_text(model="gemini-1.5-turbo", prompt=user_input)
        st.subheader("Response:")
        st.write(response.text)
    else:
        st.error("Please enter a prompt.")  