import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI 

class Model:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def openai_chatgpt(transcript, prompt, extra=""):
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_CHATGPT_API_KEY"))
        model = "gpt-4-turbo"
        message = [{"role": "system", "content": prompt + extra + transcript}]
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=message
            )
            response = completion.choices[0].message.content
            return response
        except Exception as e:
            response_error = "⚠️ There is a problem with the API key or with python module."
            return response_error,e
