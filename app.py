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
st.write('Upload a currency note or coin to get detailed information including its country, denomination, and other relevant details.')

# API configuration for Google Generative AI
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# File uploader for currency image
uploaded_file = st.file_uploader("Upload a currency note or coin image (JPG, PNG, JPEG).", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open and display the image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Currency", use_column_width=True)

    # Convert the image to a file path to send as part of the input
    image_path = pathlib.Path(uploaded_file.name)

    # Feature button for generating description
    if st.button("Get Currency Description"):
        try:
            # Generate content using the image path
            response = model.generate_content([
                "Give a description of the currency in the image. Include its country, name, denomination, and usage. If the image does not show currency, refuse to answer.",
                str(image_path)
            ])
            st.write(to_markdown(response.text).data)
        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.warning("Please upload an image of a currency first.")
