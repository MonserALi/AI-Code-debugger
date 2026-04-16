import streamlit as st
from google import genai
import os
from PIL import Image
from api_calling import generate_response


with st.sidebar:
    st.header("Controls ",anchor=None)
    images = st.file_uploader("Upload your code snippet",
         ('jpeg','png','jpg'),
        accept_multiple_files = False
    )
    
    
    if images:
        pil_images = Image.open(images)
        target_height = 190
        ratio = pil_images.width / pil_images.height
        new_width = int(target_height * ratio)
        resized_img = pil_images.resize((new_width, target_height))
        
        st.image(resized_img)

    selected = st.selectbox("How do you want solve the problem",
        ('Hint','Solution with code'),
        index=None
    )
    clicked  = st.button("Ask to AI")

st.header("Code Debugger",anchor=False)
st.text("Upload the screen shot of your code to review")
st.divider()

if clicked:

    if not images:
        st.error("Please upload a picture")
    if not selected:
        st.error("Please select one option")

    if images and selected:
        with st.container(border=True):
            with st.spinner("Please wait for a while...."):
                response = generate_response(pil_images,selected)
                st.markdown(response)

                


