import google.generativeai as genai
import os

def chat(prompt):

    genai.configure(api_key="AIzaSyCazJEmpYATyI34DZUKsHfwIoFq94yGALI")

    # Using `response_mime_type` requires one of the Gemini 1.5 Pro or 1.5 Flash models
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)
    return response.text
