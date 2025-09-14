import os
from google import genai
from dotenv import load_dotenv

def load_client():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    client = genai.Client(api_key=GOOGLE_API_KEY)
    return client
