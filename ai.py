import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from load_client import load_client
# import base64

from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = load_client()
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=list[Recipe],
        thinking_config=types.ThinkingConfig(
            # thinking_budget=0, 
            # include_thoughts=True
        ), # Disables thinking
    ),
)

#  this is for when include thoughts are on. useful for debugging
# for part in response.candidates[0].content.parts:
#   if not part.text:
#     continue
#   if part.thought:
#     print("Thought summary:")
#     print(part.text)
#     print()
#   if part.thought_signature:
#     print(base64.b64encode(part.thought_signature).decode("utf-8"))
#   else:
#     print("Answer:")
#     print(part.text)
#     print()
    
print(response.text)

# cost
# print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
# print("Output tokens:",response.usage_metadata.candidates_token_count)
# print("Total tokens:",response.usage_metadata.total_token_count)