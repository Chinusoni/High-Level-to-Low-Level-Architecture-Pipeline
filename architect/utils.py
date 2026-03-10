import os
import json
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Define the structure we want Gemini to follow
class TechSpecSchema(BaseModel):
    modules: list[str]
    database_tables: str
    logic_pseudocode: str

def generate_tech_specs(requirement):
    model_id = "gemini-3.1-flash-lite-preview"
    
    prompt = f"Convert this business requirement into a technical spec: {requirement}"

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': TechSpecSchema,
                'temperature': 0.2
            }
        )
        # Parse the JSON string into a Python Dictionary
        return json.loads(response.text)
    except Exception as e:
        print(f"Error: {e}")
        return None