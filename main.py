import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set! Please edit .env and add your API key.")

client = genai.Client(api_key=api_key)
content = client.models.generate_content(model="gemini-2.5-flash", contents="Who are you and what do you do? Respond in a single sentence.")
print(content.text)
