from google import genai
from google.genai import types
import pathlib
from load_client import load_client

client = load_client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('MarcusIcaro.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)