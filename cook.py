import streamlit as st
import pandas as pd
import google.generativeai as genai

# Set Gemini API key
genai.configure(api_key="AIzaSyB9rSb0TXKD2nv0ZwAHUGDDEWMRP87Ltns")

st.title("Recipe Generator")
st.write("I love youu Kanishh babyy!")

if st.button("Show available Gemini models"):
    try:
        models = genai.list_models()
        st.subheader("Available Models:")
        for m in models:
            st.write(m)
    except Exception as e:
        st.error(f"Error listing models: {e}")

# Input box for ingredients
ingredients = st.text_input("Enter ingredients (comma separated):")

if ingredients:
    try:
        # Set up Gemini model (assumes API key is set in environment or config)
        model = genai.GenerativeModel('gemini-pro')  # Replace with a valid model after listing
        prompt = f"Generate a recipe using these ingredients: {ingredients}. Give a title, ingredients list, and steps."
        response = model.generate_content(prompt)
        st.subheader("Generated Recipe:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error generating recipe: {e}")