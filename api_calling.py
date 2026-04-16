from google import genai
import streamlit as st
import os,io
from dotenv import load_dotenv



load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def generate_response(img,option):
    try:
        if option=="Hint":
            prompt = """based on the image find out the problem and
             give me Hints to fix this error, don't give the solution directly,
             also add the markdown to defferentiate defferent section.
             if the image is not of a code snippet then show 'The image you provided is not a code snippet '
             
             """
            response = client.models.generate_content(
             model="gemini-3-flash-preview",
             contents=[img,prompt]
            )
        if option=="Solution with code":
            prompt = """based on the image find out the problem
            and give the detail solution with 
            necessary markdown for code section and others.
            if the image is not of a code snippet then show 'The image you provided is not a code snippet '
            
            """
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[img,prompt]
            )
    except Exception as e:
        return "Sorry. Something went wrong, Check and try again.."
        print(e)
    else:
        return response.text