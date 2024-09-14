import pathlib
import textwrap
import streamlit as st
from PIL import Image
import google.generativeai as genai
from IPython.display import display, Markdown

# Helper function to format text as Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# App title and description
st.title('Currency Explorer')
st.write('Upload a currency note or coin to get detailed information including its country, denomination, and historical facts.')

# API configuration for Google Generative AI
genai.configure(api_key=st.secrets["api_key"])
model = genai.GenerativeModel('gemini-1.5-flash')

# File uploader for currency image
uploaded_file = st.file_uploader("Upload a currency note or coin image (JPG, PNG, JPEG).", type=["jpg", "png", "jpeg"])

# Feature buttons
if st.button("Get Currency Description"):
    if uploaded_file is not None:
        # Display image preview
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Currency", use_column_width=True)

        # Request description from the model
        response = model.generate_content([
            "Give a description of the currency in the image. Include its country, name, denomination, and usage. If the image does not show currency, refuse to answer.", img
        ])

        st.write(to_markdown(response.text).data)
    else:
        st.warning("Please upload an image of a currency first.")

# Optional feature: Ask for historical information
if st.button("Get Historical Information"):
    if uploaded_file is not None:
        # Request historical info from the model
        response = model.generate_content([
            "Give me some historical information about the currency shown in the image. Include important events or milestones associated with it.", img
        ])

        st.write(to_markdown(response.text).data)
    else:
        st.warning("Please upload an image of a currency first.")
