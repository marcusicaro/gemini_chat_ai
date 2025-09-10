import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Prompt here",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)