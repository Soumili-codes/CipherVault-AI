

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def ask_ai(question):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return response.text
