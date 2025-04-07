# openai_client.py
import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')

        if not api_key or not api_key.startswith('sk-proj-') or len(api_key) <= 10:
            raise ValueError("There might be a problem with your API key. Please check your .env file.")
        
        self.client = OpenAI(api_key=api_key)

    def chat(self, model: str, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
